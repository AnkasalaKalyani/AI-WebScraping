import streamlit as st
from src.services import scrape_and_store_product, fetch_and_store_competitors
from src.db import Database
from src.llm import analyze_competitors


def render_header():
    st.title("Amazon Competitor Analysis")
    st.caption("Enter your ASIN to get product insights.")


def render_inputs():
    asin = st.text_input("ASIN", placeholder="e.g., B0FVTLHRKJ")
    geo = st.text_input("Zip/Postal Code", placeholder="e.g., 10001")
    domain = st.selectbox(
        "Domain",
        ["com", "ca", "co.uk", "de", "fr", "it", "ae"]
    )

    return asin.strip(), geo.strip(), domain


def render_product_card(product):
    with st.container(border=True):

        cols = st.columns([1, 2])

        # Image
        try:
            images = product.get("images", [])

            if images:
                cols[0].image(images[0], width=200)
            else:
                cols[0].write("No image found.")
        except Exception:
            cols[0].write("Error loading image.")

        # Product details
        with cols[1]:
            asin = product.get("asin")
            title = product.get("title")

            st.subheader(title or asin or "Unknown Product")

            info_cols = st.columns(3)

            currency = product.get("currency", "")
            price = product.get("price", "-")

            info_cols[0].metric(
                "Price",
                f"{currency} {price}" if currency else str(price)
            )

            info_cols[1].write(
                f"**Brand:** {product.get('brand', '-')}"
            )

            info_cols[2].write(
                f"**Rating:** {product.get('rating', '-')}"
            )

            domain_info = f"amazon.{product.get('amazon_domain', 'com')}"
            geo_info = product.get("geo_location", "-")

            st.caption(
                f"Domain: {domain_info} | Geo Location: {geo_info}"
            )

            if product.get("url"):
                st.write(product["url"])

            if asin:
                if st.button(
                    "Start Analyzing Competitors",
                    key=f"analyze_{asin}"
                ):
                    st.session_state["analyzing_asin"] = asin
            else:
                st.warning("ASIN not available for this product.")


def main():
    st.set_page_config(
        page_title="Amazon Competitor Analysis",
        page_icon="📦",
        layout="wide"
    )

    render_header()

    asin, geo, domain = render_inputs()

    # Scrape Product
    if st.button("Scrape Product"):

        if not asin:
            st.error("Please enter an ASIN.")
        elif len(asin) != 10:
            st.error("ASIN should be 10 characters long.")
        else:
            with st.spinner("Scraping product..."):
                scrape_and_store_product(
                    asin,
                    geo,
                    domain
                )

            st.success("Product scraped successfully!")

    # Load Products
    db = Database()
    products = db.get_all_products()

    if products:
        st.divider()
        st.subheader("Products Scraped")

        items_per_page = 10

        total_pages = (
            len(products) + items_per_page - 1
        ) // items_per_page

        _, page_col, _ = st.columns([2, 3, 2])

        with page_col:
            page = (
                st.number_input(
                    "Page",
                    min_value=1,
                    max_value=max(total_pages, 1),
                    value=1
                )
                - 1
            )

        start_idx = page * items_per_page
        end_idx = min(
            start_idx + items_per_page,
            len(products)
        )

        st.write(
            f"Showing {start_idx + 1} - {end_idx} "
            f"of {len(products)} products"
        )

        for product in products[start_idx:end_idx]:
            render_product_card(product)

    # Competitor Analysis
    selected_asin = st.session_state.get("analyzing_asin")

    if selected_asin:
        st.divider()

        st.subheader(
            f"Competitor Analysis for {selected_asin}"
        )

        existing_comps = db.search_products(
            {"parent_asin": selected_asin}
        )

        if not existing_comps:
            with st.spinner("Searching competitors..."):
                comps = fetch_and_store_competitors(
                    selected_asin,
                    domain,
                    geo
                )

            st.success(
                f"Found {len(comps)} competitors!"
            )
        else:
            st.info(
                f"Found {len(existing_comps)} competitors in the database."
            )

        col1, col2 = st.columns([3, 1])

        with col2:
            if st.button("Refresh Competitors"):
                with st.spinner("Refreshing competitors..."):
                    comps = fetch_and_store_competitors(
                        selected_asin,
                        domain,
                        geo
                    )

                st.success(
                    f"Found {len(comps)} competitors!"
                )

        with col1:
            if st.button(
                "Analyze with LLM",
                type="primary"
            ):
                try:
                    with st.spinner("Running LLM analysis..."):
                        analysis = analyze_competitors(
                            selected_asin
                        )

                    st.success("Analysis completed!")
                    st.markdown("### AI Analysis")
                    st.text(analysis)

                except Exception as e:
                    st.error(
                        f"LLM Analysis failed: {str(e)}"
                    )


if __name__ == "__main__":
    main()
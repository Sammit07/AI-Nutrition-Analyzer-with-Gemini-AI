"""
Streamlit Food Nutrition Analyzer
Upload food images and get detailed nutritional analysis using Gemini AI
"""

from io import BytesIO

import google.generativeai as genai
import streamlit as st
from PIL import Image

# Page configuration
st.set_page_config(
    page_title="AI Nutrition Analyzer",
    page_icon="🍽️",
    layout="wide"
)

# System prompt for Gemini
SYSTEM_PROMPT = """You are a certified nutrition analyst. You receive (a) a single food image and (b) optional user notes.
Your tasks:
1) Identify the food items present. If uncertain, state assumptions explicitly.
2) Estimate portion sizes (grams or common household measures) as seen; if uncertain, give a conservative range and say why.
3) Provide calories per item and a total calorie estimate.
4) Include macronutrient breakdown per item when reasonably inferable (protein, carbs, fat in grams).
5) Flag allergens or dietary considerations (e.g., nuts, dairy, gluten) if likely present; explain uncertainty.
6) Offer healthier swap suggestions or portion guidance for common goals (weight loss, maintenance, muscle gain)—keep it brief and practical.

Formatting (use exactly this structure):
- Items Detected:
  1) <Item name> — ~<portion> — ~<kcal> kcal
     • Macros (est.): P ~x g, C ~y g, F ~z g
  2) ...

- Assumptions & Uncertainty:
  • <short bullet on any visual ambiguity and its impact on estimates>

- Total Estimated Calories: ~<sum> kcal

- Notes & Tips:
  • <one-line practical advice or swap>
  • <one-line safety/allergen caveat if relevant>

Constraints & Behavior:
- If visibility is poor or items are occluded, say so and provide a best-effort range.
- Do not invent precise values when uncertain; provide ranges and label them.
- Prefer standard reference foods and typical preparation methods unless user notes say otherwise.
- Be concise but complete. Avoid long paragraphs; prefer clean bullets."""


def initialize_gemini():
    """Initialize Gemini with API key from environment."""
    import os

    from dotenv import load_dotenv

    # Load environment variables from .env file
    load_dotenv()
    
    # Configure Gemini
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    
    
    return genai.GenerativeModel('gemini-2.5-pro')


def analyze_food_image(model, image, user_notes=None):
    """Analyze food image using Gemini."""
    try:
        # Prepare prompt
        user_message = f"User notes: {user_notes}" if user_notes else "No additional notes provided."
        full_prompt = f"{SYSTEM_PROMPT}\n\n{user_message}"
        
        # Generate analysis
        response = model.generate_content([full_prompt, image])
        
        return {
            "success": True,
            "analysis": response.text
        }
    
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }


def main():
    # Header
    st.title("🍽️ AI Nutrition Analyzer")
    st.markdown("### Powered by Google Gemini")
    st.markdown("---")
    
    # Initialize Gemini
    model = initialize_gemini()
    
    # Sidebar
    with st.sidebar:
        st.header("📋 About")
        st.markdown("""
        This app uses **Google Gemini AI** to analyze food images and provide:
        - 🔍 Food item identification
        - ⚖️ Portion size estimates
        - 📊 Calorie & macro breakdown
        - ⚠️ Allergen warnings
        - 💡 Healthier alternatives
        """)
        
        st.markdown("---")
        st.header("⚙️ Settings")
        
        # Goal selection
        goal = st.selectbox(
            "Health Goal",
            ["General Info", "Weight Loss", "Muscle Gain", "Maintenance"]
        )
        
        st.markdown("---")
        st.markdown("**Made with ❤️ using Streamlit & Gemini**")
    
    # Main content area
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.header("📸 Upload Food Image")
        
        # File uploader
        uploaded_file = st.file_uploader(
            "Choose an image...",
            type=['png', 'jpg', 'jpeg', 'webp'],
            help="Upload a clear photo of your food"
        )
        
        # Additional notes
        user_notes = st.text_area(
            "📝 Additional Notes (optional)",
            placeholder="E.g., 'Homemade pasta with olive oil' or 'Restaurant serving'",
            height=100
        )
        
        # Add goal to notes if specified
        if goal != "General Info":
            if user_notes:
                user_notes += f" | Goal: {goal}"
            else:
                user_notes = f"Goal: {goal}"
        
        # Display uploaded image
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", use_container_width=True)
            
            # Analyze button
            if st.button("🔍 Analyze Nutrition", type="primary", use_container_width=True):
                with st.spinner("🤖 Analyzing your food..."):
                    result = analyze_food_image(model, image, user_notes)
                    
                    # Store result in session state
                    st.session_state['result'] = result
        else:
            st.info("👆 Upload an image to get started")
    
    with col2:
        st.header("📊 Nutrition Analysis")
        
        # Display results
        if 'result' in st.session_state:
            result = st.session_state['result']
            
            if result['success']:
                # Success - display analysis
                st.success("✅ Analysis complete!")
                
                # Display in a nice container
                with st.container():
                    st.markdown(result['analysis'])
                
                # Download button
                st.download_button(
                    label="📥 Download Analysis",
                    data=result['analysis'],
                    file_name="nutrition_analysis.txt",
                    mime="text/plain"
                )
                
            else:
                # Error
                st.error(f"❌ Analysis failed: {result['error']}")
                st.info("Please try again or check your API key.")
        else:
            # No results yet
            st.info("👈 Upload an image and click 'Analyze Nutrition' to see results here")
            
            # Show example
            with st.expander("📖 See Example Output"):
                st.markdown("""
                **Items Detected:**
                1) Grilled Chicken Breast — ~150g — ~250 kcal
                   • Macros (est.): P ~45g, C ~0g, F ~5g
                2) Brown Rice — ~1 cup (195g) — ~215 kcal
                   • Macros (est.): P ~5g, C ~45g, F ~2g
                3) Steamed Broccoli — ~100g — ~35 kcal
                   • Macros (est.): P ~3g, C ~7g, F ~0g
                
                **Assumptions & Uncertainty:**
                • Chicken appears grilled with minimal oil; actual calories may vary by ±10% based on cooking method
                • Rice portion estimated from plate proportion; could be 170-220g range
                
                **Total Estimated Calories:** ~500 kcal
                
                **Notes & Tips:**
                • Well-balanced meal with good protein and fiber; consider adding healthy fats (avocado, nuts)
                • No major allergens detected; broccoli and rice are gluten-free
                """)


if __name__ == "__main__":
    main()
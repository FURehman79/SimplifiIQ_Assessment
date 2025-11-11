import argparse
import pandas as pd
import requests
from bs4 import BeautifulSoup
import os
import google.generativeai as genai
import os
os.environ["GEMINI_API_KEY"] = "AIzaSyDfUCuHj9uTcl2EDpUg_bJzRJ5PaJDGawA"

# Function to extract title and meta
def extract_page_info(url, use_network=False):
    if not use_network:
        # Mock mode data
        return {
            "title": f"Title of {url.split('//')[-1].split('.')[0]}",
            "meta": f"Meta of {url.split('//')[-1].split('.')[0]}"
        }
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string if soup.title else "N/A"
        meta = soup.find('meta', attrs={'name': 'description'})
        meta_desc = meta['content'] if meta and 'content' in meta.attrs else "N/A"
        return {"title": title, "meta": meta_desc}
    except Exception as e:
        return {"title": "Error", "meta": str(e)}

# Gemini-based summary generation
def generate_summary_with_gemini(title, meta):
    try:
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        prompt = f"Summarize this webpage in 2 short professional sentences.\nTitle: {title}\nMeta Description: {meta}"
        model = genai.GenerativeModel("models/gemini-2.5-flash")

        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error: {e}"

# Main script logic
def main(input_file, output_file, use_network=False):
    df = pd.read_csv(input_file)
    results = []

    for _, row in df.iterrows():
        url = row['url']
        info = extract_page_info(url, use_network)
        title = info['title']
        meta = info['meta']

        if use_network:
            summary = generate_summary_with_gemini(title, meta)
        else:
            summary = f"MOCK SUMMARY: {title} - {meta}"

        results.append({
            "url": url,
            "title": title,
            "meta": meta,
            "summary": summary
        })

    out_df = pd.DataFrame(results)
    out_df.to_csv(output_file, index=False)
    print(f"\n✅ Automation Completed — Results saved to {output_file}\n")
    print(out_df.head())

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Web Automation + Summarization Script")
    parser.add_argument("--input", required=True, help="Input CSV file containing URLs")
    parser.add_argument("--output", required=True, help="Output CSV file for results")
    parser.add_argument("--use-network", action="store_true", help="Use real web + Gemini API mode")
    args = parser.parse_args()
    main(args.input, args.output, args.use_network)

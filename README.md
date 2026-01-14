# IT4142E – Introduction to Data Science (2025)
## Clustering YouTube Channels Using User Comments

This project builds a large-scale dataset from YouTube user comments to **discover and map communities of YouTube channels**. We scraped commenter information and comment text across **800+ channels**, collecting **13+ million comments** in total. During preprocessing, **~3 million comments** were flagged as spam/useless and removed before downstream analysis. :contentReference[oaicite:1]{index=1}

A major challenge was YouTube Data API quota constraints; to complete the crawl efficiently, the team crowdsourced and used **29 YouTube API keys**, finishing the scraping process within **~2 days**. :contentReference[oaicite:2]{index=2}

---

## Folder Structure

Project_DataSciense_2025_1/
├─ data/
│  ├─ Cluster_E5.csv
│  ├─ Cluster_MiniLM.csv
│  ├─ 1697_channels_to_scrape.csv
│  ├─ channels_e5-small.txt
│  └─ channels_all-MiniLM-L6-v2.txt
├─ notebooks/
│  ├─ main.ipynb
│  ├─ Embed.ipynb
│  └─ scraw_youtube(v3).ipynb
└─ embeddings/
   ├─ channel_embeddings_e5-small.npy
   └─ channel_embeddings_all-MiniLM-L6-v2.npy

---

## Pipeline (Recommended Order)

1. **Scrape YouTube data**
   - Notebook: `notebooks/scraw_youtube(v3).ipynb`
   - Input: `data/1697_channels_to_scrape.csv`

2. **Generate embeddings**
   - Notebook: `notebooks/Embed.ipynb`
   - Inputs:
     - `data/channels_e5-small.txt`
     - `data/channels_all-MiniLM-L6-v2.txt`
   - Outputs:
     - `embeddings/channel_embeddings_e5-small.npy`
     - `embeddings/channel_embeddings_all-MiniLM-L6-v2.npy`

3. **Clustering & analysis**
   - Notebook: `notebooks/main.ipynb`
   - Outputs:
     - `data/Cluster_E5.csv`
     - `data/Cluster_MiniLM.csv`

---

## Methods & Key Results

### K-means clustering (baseline)
We used K-means on channel representations and identified **~10 communities**, including at least **two music-related communities**. :contentReference[oaicite:3]{index=3}

### Semantic debiased clustering (two-stage)
We also implemented a “precision-first” semantic pipeline:
- Embedding comments with a multilingual sentence transformer
- Global semantic reweighting (Anchor-IDF style)
- Channel-level aggregation
- Stage-1 clustering with **HDBSCAN** to find high-confidence semantic cores
- Stage-2 hierarchical clustering to refine and assign remaining channels
- Validation + visualization (dimensionality reduction) :contentReference[oaicite:4]{index=4}

With this second clustering approach, we obtained **12 channel clusters**. :contentReference[oaicite:5]{index=5}

---

## Acknowledgements
This project is built by a group of students at Hanoi University of Science and Technology, Vietnam. Thanks for the contribution from Hoang Trung Dung, Le Minh Kiet, Le Tam Quang, Nguyen Vu Thuy, Nguyen Tat Hung. These authors contributed equally. The order is arbitrary.

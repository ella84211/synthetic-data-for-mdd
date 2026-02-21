# Synthetic Data for Mispronunciation Detection and Diagnosis

## Setup

```
git clone https://github.com/ella84211/synthetic-data-for-mdd.git
cd synthetic-data-for-mdd
pip install -r requirements.txt
```

## Preprocessing speechocean762 data
Make the directory
```
mkdir real_data
```

Get the speechocean762 data
```
git clone https://github.com/jimbozhang/speechocean762.git
cp speechocean762/resource/scores.json real_data
```

Run the scripts to preprocess the data
```
python preprocess_speechocean762.py
python split_speechocean762.py
```
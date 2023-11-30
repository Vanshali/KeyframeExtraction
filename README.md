# A Multi-Scale Attention Framework for Automated Polyp Localization and Keyframe Extraction From Colonoscopy Videos

Paper Link: [https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=10268934](https://ieeexplore.ieee.org/abstract/document/10268934/)

## 1. Introduction
Colonoscopy video acquisition has been tremendously increased for retrospective analysis, comprehensive inspection, and detection of polyps to diagnose colorectal cancer (CRC). However, extracting meaningful clinical information from
colonoscopy videos requires an enormous amount of reviewing time, which burdens the surgeons considerably. To reduce the manual efforts, we propose a first end-to-end automated multi-stage deep learning framework to extract an adequate number of clinically significant frames, i.e., keyframes from colonoscopy videos. The proposed framework comprises multiple stages that employ different deep learning models to select keyframes, which are high-quality, non-redundant polyp frames capturing multi-views of polyps. In one of the stages of our framework, we also propose a novel multi-scale attention-based model, **YcOLOn**, for polyp localization, which generates ROI and prediction scores crucial for obtaining keyframes. 

## 2. Framework Overview
![Flowchart depicting the role of different stages in the proposed work](figures/framework.png)
*Figure 1:  Flowchart depicting the role of different stages in the proposed work.*

## 3. YcOLOn Architecture
![Different components of the proposed model.](figures/YcOLOn.png)
*Figure 2: Different components of the proposed model. AFF is the attention feature fusion module, and MS-CAM is the multi-scale channel attention component of the AFF.*

## 4. Results
### 4.1 Stage-I: Quality Assessment
![Stage-I](figures/Table1.png)

### 4.2 Stage-II: Polyp Detection
![Stage-IIa](figures/Table2.png)
![Stage-IIb](figures/Table3.png)

### 4.3 Stage-III and Stage-IV: Redundancy Removal and Polyp Localization
![Stage-IV](figures/Table4.png)
![Score graph](figures/score_graph.png)

## 5. Usage

## 6. Citation:
```
@article{sharma2023multi,
  title={A Multi-Scale Attention Framework for Automated Polyp Localization and Keyframe Extraction From Colonoscopy Videos},
  author={Sharma, Vanshali and Sasmal, Pradipta and Bhuyan, MK and Das, Pradip K and Iwahori, Yuji and Kasugai, Kunio},
  journal={IEEE Transactions on Automation Science and Engineering},
  year={2023},
  publisher={IEEE}
}
```

This repository will be updated soon!

# Food Knowledge Triple Dataset / 食物知识三元组数据集

一个面向知识图谱、自然语言处理与相关研究实验的中文食物知识三元组数据集。当前版本将原始 CSV 中可明确识别的完整三元组标准化为 `subject, relation, object` 三列，并完整保留原始文件与待人工核查记录。

> **推荐使用文件：** `data/processed/food_triples.csv`  
> 该文件包含 **2032 条精确去重后的完整三元组**。

## 项目人员 / Project Team

- **数据集作者与维护者 / Dataset Author & Maintainer：** 李承罡（Li Chenggang；英文名/别名：`just`）
- **单位 / Affiliation：** 甘肃农业大学 机电工程学院（College of Mechanical and Electrical Engineering, Gansu Agricultural University）
- **学术指导 / Academic Advisor：** 杨婉霞
- **合作者 / Contributor：** 张源浩
- **公开联系邮箱 / Public Email：** 未提供

> 说明：导师与合作者在本仓库中按“学术指导”和“合作者”列示，并不自动等同于论文或数据集的共同署名作者。若后续确定共同作者关系，应依据实际学术贡献与团队约定同步更新 `CITATION.cff`。

## 数据概览

| 指标 | 数量 |
|---|---:|
| 原始数据行 | 3625 |
| 完整三元组记录（含重复） | 3539 |
| 精确去重后的三元组 | 2032 |
| 精确重复的额外记录 | 1507 |
| 重复三元组组数 | 957 |
| 不完整记录 | 86 |
| 唯一 subject | 422 |
| 唯一 object | 946 |
| subject/object 合并后的唯一节点 | 947 |

### 关系类型

去重后的关系分布：

| relation | 数量 | 含义 |
|---|---:|---|
| 名称 | 422 | 食物类别或上位概念与具体食物名称之间的关系 |
| 外形 | 672 | 与外观、形态或视觉描述相关的关系 |
| 口感 | 570 | 与质地、咀嚼体验或口感描述相关的关系 |
| 味道 | 368 | 与味觉、气味或风味描述相关的关系 |

## 数据格式

推荐文件 `data/processed/food_triples.csv` 使用 UTF-8 编码，格式如下：

```csv
subject,relation,object
食物,名称,佛跳墙
佛跳墙,味道,腥味
食物,名称,炒杏鲍菇
```

三列定义：

- `subject`：三元组头实体/主语。
- `relation`：关系类型，当前为 `名称`、`外形`、`口感`、`味道` 四类。
- `object`：三元组尾实体/属性值。

## 仓库结构

```text
food-knowledge-triples/
├── README.md
├── LICENSE
├── CITATION.cff
├── metadata.json
├── data/
│   ├── raw/
│   │   └── food_triples_original.csv
│   └── processed/
│       ├── food_triples.csv
│       └── food_triples_all_complete.csv
├── data_review/
│   ├── incomplete_rows.csv
│   ├── unassigned_values.csv
│   ├── missing_object_rows.csv
│   └── blank_rows.csv
├── reports/
│   ├── data_quality_report.md
│   └── duplicate_groups.csv
├── docs/
│   ├── data_description.md
│   └── PUBLISH_CHECKLIST.md
└── scripts/
    ├── prepare_dataset.py
    └── validate_dataset.py
```

## 文件说明

- `data/raw/food_triples_original.csv`：原始上传文件的逐字节副本，不做修改。
- `data/processed/food_triples.csv`：**推荐版本**。仅保留完整记录，并对完全相同的三元组进行精确去重。
- `data/processed/food_triples_all_complete.csv`：所有完整三元组，保留重复记录，可用于需要频次信息的实验。
- `data_review/incomplete_rows.csv`：全部 86 条不完整记录，保留原始行号。
- `reports/duplicate_groups.csv`：所有重复三元组及出现次数。
- `metadata.json`：机器可读的数据集统计元数据。

## 数据清洗原则

本版本只进行了**结构性清洗**，没有对语义内容进行主观纠正：

1. 删除原 CSV 中仅作为行号使用的索引列。
2. 将 `A / B / C` 重命名为 `subject / relation / object`。
3. 完整三元组要求三列均非空。
4. 推荐文件只做“完全相同三元组”的精确去重，不进行同义词合并、语义修正或人工补全。
5. 所有无法安全自动判断的记录均保留在 `data_review/`，没有直接删除。
6. 原始文件完整保留，以确保可追溯性。

这意味着数据中仍可能存在语义噪声、抽取误差或关系标注不完全合理的情况。正式论文实验前建议结合你的研究任务进一步人工核验。

## 快速使用

Python 标准库：

```python
import csv

with open("data/processed/food_triples.csv", encoding="utf-8") as f:
    triples = list(csv.DictReader(f))

print(triples[0])
```

Pandas 用户可以直接：

```python
import pandas as pd

df = pd.read_csv("data/processed/food_triples.csv")
print(df.head())
```

## 复现清洗

原始数据的清洗过程可通过以下脚本复现：

```bash
python scripts/prepare_dataset.py
python scripts/validate_dataset.py
```

## 数据来源与公开前确认

仓库结构和数据清洗已完成，但**数据来源/采集授权信息必须由数据持有人最终确认**。如果原始内容来自第三方网站、论文数据集、API、爬虫或其他知识库，请在公开前确认其许可条款，并在本 README 或 `docs/data_description.md` 中补充来源与必要署名。

不要将你无权再许可的第三方内容声明为自己的原创数据。

## License

本仓库默认按 **Creative Commons Attribution 4.0 International (CC BY 4.0)** 组织许可信息，**仅适用于仓库贡献者有权许可的内容**。第三方内容仍受其原始权利和许可约束。详见 `LICENSE`。

## Citation

仓库包含 `CITATION.cff`。GitHub 在默认分支识别该文件后，可显示 **Cite this repository**。

当前 `CITATION.cff` 将 **李承罡（Li Chenggang）**列为数据集引用作者，单位为 **College of Mechanical and Electrical Engineering, Gansu Agricultural University**。英文名/别名 `just` 作为 alias 保留。

学术指导 **杨婉霞** 与合作者 **张源浩** 已在本 README 的项目人员部分列示，但目前**没有自动加入 `CITATION.cff` 的 `authors` 列表**，以避免在未确认共同署名关系时将“指导/合作”直接等同于“引用作者”。如果团队确认三人均应作为数据集共同作者，应在正式发布前同步调整 `CITATION.cff`。

创建 GitHub 仓库后，还可以在 `CITATION.cff` 中补充仓库 URL（`repository-code`）或后续 DOI。

## Version

- `v1.0.0` — 2026-09-11：首次标准化整理版本。

---

### English summary

This repository contains a Chinese food knowledge triple dataset with four relation types: food name, appearance, texture, and taste. The recommended processed file is `data/processed/food_triples.csv`, containing 2032 exact-deduplicated complete triples. The original file and all incomplete records are preserved for traceability and manual review. The dataset author and maintainer is **Li Chenggang (alias: just)**, affiliated with the **College of Mechanical and Electrical Engineering, Gansu Agricultural University**. **杨婉霞** is listed as academic advisor and **张源浩** as contributor in the repository documentation.

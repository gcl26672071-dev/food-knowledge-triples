# GitHub 公开前检查清单

仓库文件已经整理完成。正式将 GitHub 仓库从 Private 改成 Public 之前，建议逐项确认：

- [ ] 已确认原始数据的来源，以及你有权公开/再许可这些内容。
- [ ] 如果数据来自第三方，已在 README 或 `docs/data_description.md` 写明来源、许可与署名。
- [ ] 已人工查看 `data_review/incomplete_rows.csv`，决定是否需要补全、删除或另行分类。
- [ ] 已抽样检查 `data/processed/food_triples.csv` 的语义质量。
- [ ] 已确认是否需要保留重复记录；默认推荐使用去重版。
- [ ] 已检查仓库不存在密码、API Key、账号令牌、个人隐私信息或未公开的机密研究材料。
- [ ] 已确认 CC BY 4.0 适合你的公开目标；如不适合，请在公开前替换 `LICENSE` 和 `CITATION.cff` 中的许可字段。
- [x] `CITATION.cff` 已填写数据集作者李承罡（Li Chenggang）及单位信息；导师与合作者已在 README 中按角色列示。
- [ ] 创建 GitHub 仓库后，可在 `CITATION.cff` 补充 `repository-code` 或 DOI（可选）。
- [ ] 建议创建 GitHub Release：`v1.0.0`。

## 最简上传方式

1. GitHub 新建仓库，建议仓库名：`food-knowledge-triples`。
2. 初始状态选择 **Private**。
3. 将本目录中的所有文件和文件夹上传到仓库根目录。
4. 检查 README 在 GitHub 页面展示是否正常。
5. 检查数据文件和 `CITATION.cff`。
6. 确认来源/许可后，再把仓库 Visibility 改为 **Public**。

## 建议的首次提交说明

```text
Initial release of food knowledge triple dataset v1.0.0
```

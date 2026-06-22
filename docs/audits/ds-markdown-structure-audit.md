# DS記事 Markdown構造・レンダリング監査レポート
## 1. サマリー
- 対象: `pages/ds/**/*.md`
- チェックしたDS Markdownファイル数: **285**
- 優先度付き候補数: **54件**（高: **4件** / 中: **20件** / 低: **30件**）
- 手動フッター移行候補: **242件**
- 監査方針: front matterを除いた本文を対象に、見出し、水平線、旧式スキル項目、標準見出しとの差分、front matter風テキスト混入、手動フッター残存を確認した。
- 注意: 本タスクではDS記事ファイルを編集していない。本文修正案は今後の対応方向のみを示す。
## 2. 高優先度候補（表示・意味が崩れる可能性）
| ファイル | 種別 | 行 | 抜粋 | 説明・修正方向 |
| --- | --- | ---: | --- | --- |
| `pages/ds/association-metrics.md` | 疑わしい見出し（式の分子がH2化） | 117 | `## XとYの共起回数` | 式の分子・分母説明は見出しではなく本文または箇条書きに寄せる。 |
| `pages/ds/customer-journey.md` | 本文へのfront matter風テキスト混入 | 249 | `tags: [ds, business, marketing]` | 本文末尾などに残ったメタデータ行を削除する。 |
| `pages/ds/regular-expression-email.md` | 本文へのfront matter風テキスト混入 | 21 | `tags: [ds, preprocessing, cheatsheet]` | 本文末尾などに残ったメタデータ行を削除する。 |
| `pages/ds/sql-in-exists.md` | 本文へのfront matter風テキスト混入 | 186 | `tags: [ds, preprocessing, database]` | 本文末尾などに残ったメタデータ行を削除する。 |

## 3. 中優先度候補（旧構造・視認性・標準化）
| ファイル | 種別 | 行 | 抜粋 | 説明・修正方向 |
| --- | --- | ---: | --- | --- |
| `pages/ds/ab-test.md` | 対応スキル項目の旧式表記 | 199 | `【対応スキル項目（ビジネス力シート）】` | `## 対応スキル項目（...）` の見出し形式へ統一する。 |
| `pages/ds/ab-test.md` | 本文中の水平線が多い | 27 | `12本（例: 27, 74, 90, 101, 111, 123行目）` | 見出しで区切れる箇所は水平線を減らし、視覚ノイズを下げる。 |
| `pages/ds/customer-journey.md` | 対応スキル項目の旧式表記 | 189 | `【対応スキル項目（ビジネス力シート）】` | `## 対応スキル項目（...）` の見出し形式へ統一する。 |
| `pages/ds/customer-journey.md` | 本文中の水平線が多い | 27 | `13本（例: 27, 50, 68, 81, 93, 105行目）` | 見出しで区切れる箇所は水平線を減らし、視覚ノイズを下げる。 |
| `pages/ds/data-driven.md` | 標準6見出しとの差分が大きい | 11 | `## 定義・仕組み, ## どんな場面で使う？, ## よくある誤解・混同, ## まとめ（試験直前用）` | 通常個別記事として標準見出しへ寄せるか、特殊記事として役割を明確化する。 |
| `pages/ds/data-literacy-practice.md` | 標準6見出しとの差分が大きい | 11 | `## 定義・仕組み, ## どんな場面で使う？, ## よくある誤解・混同` | 通常個別記事として標準見出しへ寄せるか、特殊記事として役割を明確化する。 |
| `pages/ds/data-warehouse-vs-datamart.md` | 本文中の水平線が多い | 30 | `9本（例: 30, 62, 90, 106, 113, 123行目）` | 見出しで区切れる箇所は水平線を減らし、視覚ノイズを下げる。 |
| `pages/ds/dwh-appliance.md` | 本文中の水平線が多い | 28 | `9本（例: 28, 59, 91, 107, 125, 147行目）` | 見出しで区切れる箇所は水平線を減らし、視覚ノイズを下げる。 |
| `pages/ds/ffp.md` | 本文中の水平線が多い | 26 | `8本（例: 26, 42, 89, 102, 127, 145行目）` | 見出しで区切れる箇所は水平線を減らし、視覚ノイズを下げる。 |
| `pages/ds/ffp.md` | 標準6見出しとの差分が大きい | 12 | `## 定義・仕組み, ## どんな場面で使う？, ## よくある誤解・混同` | 通常個別記事として標準見出しへ寄せるか、特殊記事として役割を明確化する。 |
| `pages/ds/hypothesis-thinking.md` | 標準6見出しとの差分が大きい | 11 | `## 定義・仕組み, ## どんな場面で使う？, ## よくある誤解・混同, ## まとめ（試験直前用）` | 通常個別記事として標準見出しへ寄せるか、特殊記事として役割を明確化する。 |
| `pages/ds/morphological-dependency-parsing.md` | 本文中の水平線が多い | 28 | `8本（例: 28, 67, 99, 129, 158, 183行目）` | 見出しで区切れる箇所は水平線を減らし、視覚ノイズを下げる。 |
| `pages/ds/optional-math-algorithm.md` | 標準6見出しとの差分が大きい | 11 | `## 定義・仕組み, ## どんな場面で使う？, ## よくある誤解・混同` | 通常個別記事として標準見出しへ寄せるか、特殊記事として役割を明確化する。 |
| `pages/ds/regular-expression-email.md` | 本文中の水平線が多い | 16 | `9本（例: 16, 29, 59, 85, 103, 115行目）` | 見出しで区切れる箇所は水平線を減らし、視覚ノイズを下げる。 |
| `pages/ds/regular-expression-postalcode.md` | 本文中の水平線が多い | 22 | `9本（例: 22, 46, 70, 90, 98, 104行目）` | 見出しで区切れる箇所は水平線を減らし、視覚ノイズを下げる。 |
| `pages/ds/social-data-ai-utilization.md` | 標準6見出しとの差分が大きい | 11 | `## 定義・仕組み, ## どんな場面で使う？, ## よくある誤解・混同` | 通常個別記事として標準見出しへ寄せるか、特殊記事として役割を明確化する。 |
| `pages/ds/sora-ame-kasa.md` | 本文中の水平線が多い | 60 | `11本（例: 60, 74, 86, 101, 117, 127行目）` | 見出しで区切れる箇所は水平線を減らし、視覚ノイズを下げる。 |
| `pages/ds/sql-count-distinct.md` | 本文中の水平線が多い | 26 | `9本（例: 26, 58, 90, 115, 141, 168行目）` | 見出しで区切れる箇所は水平線を減らし、視覚ノイズを下げる。 |
| `pages/ds/sql-in-exists.md` | 対応スキル項目の旧式表記 | 126 | `【対応スキル項目（データエンジニアリング力シート）】` | `## 対応スキル項目（...）` の見出し形式へ統一する。 |
| `pages/ds/sql-in-exists.md` | 本文中の水平線が多い | 22 | `11本（例: 22, 38, 54, 70, 84, 94行目）` | 見出しで区切れる箇所は水平線を減らし、視覚ノイズを下げる。 |

## 4. 低優先度候補（後回しでよい表記ゆれ）
| ファイル | 種別 | 行 | 抜粋 | 説明・修正方向 |
| --- | --- | ---: | --- | --- |
| `pages/ds/analysis-approach-design.md` | 短すぎる小見出し | 169 | `### 誤解①  ` | 誤解の内容まで見出しに含める（例: `### 誤解①：〇〇と混同しない`）。 |
| `pages/ds/anonymized-information.md` | 短すぎる小見出し | 145 | `### 誤解①  ` | 誤解の内容まで見出しに含める（例: `### 誤解①：〇〇と混同しない`）。 |
| `pages/ds/apriori-algorithm.md` | 短すぎる小見出し | 164 | `誤解①` | 誤解の内容まで見出しに含める（例: `### 誤解①：〇〇と混同しない`）。 |
| `pages/ds/association-metrics.md` | 短すぎる小見出し | 187 | `### 誤解①` | 誤解の内容まで見出しに含める（例: `### 誤解①：〇〇と混同しない`）。 |
| `pages/ds/authentication-authorization.md` | 短すぎる小見出し | 180 | `### 誤解①  ` | 誤解の内容まで見出しに含める（例: `### 誤解①：〇〇と混同しない`）。 |
| `pages/ds/cap-theorem.md` | 短すぎる小見出し | 133 | `### 誤解①  ` | 誤解の内容まで見出しに含める（例: `### 誤解①：〇〇と混同しない`）。 |
| `pages/ds/ccpa.md` | 短すぎる小見出し | 171 | `### 誤解①  ` | 誤解の内容まで見出しに含める（例: `### 誤解①：〇〇と混同しない`）。 |
| `pages/ds/cnn.md` | 短すぎる小見出し | 174 | `誤解①` | 誤解の内容まで見出しに含める（例: `### 誤解①：〇〇と混同しない`）。 |
| `pages/ds/contract-ukeoi-juninin.md` | 短すぎる小見出し | 153 | `### 誤解①  ` | 誤解の内容まで見出しに含める（例: `### 誤解①：〇〇と混同しない`）。 |
| `pages/ds/convolution.md` | 短すぎる小見出し | 172 | `誤解①` | 誤解の内容まで見出しに含める（例: `### 誤解①：〇〇と混同しない`）。 |
| `pages/ds/curse-of-dimensionality.md` | 短すぎる小見出し | 193 | `### 誤解①  ` | 誤解の内容まで見出しに含める（例: `### 誤解①：〇〇と混同しない`）。 |
| `pages/ds/data-augmentation.md` | 短すぎる小見出し | 167 | `誤解①` | 誤解の内容まで見出しに含める（例: `### 誤解①：〇〇と混同しない`）。 |
| `pages/ds/digital-image-representation.md` | 短すぎる小見出し | 253 | `誤解①` | 誤解の内容まで見出しに含める（例: `### 誤解①：〇〇と混同しない`）。 |
| `pages/ds/elsi.md` | 短すぎる小見出し | 141 | `### 誤解①  ` | 誤解の内容まで見出しに含める（例: `### 誤解①：〇〇と混同しない`）。 |
| `pages/ds/image-filter-processing.md` | 短すぎる小見出し | 161 | `### 誤解①  ` | 誤解の内容まで見出しに含める（例: `### 誤解①：〇〇と混同しない`）。 |
| `pages/ds/interpret-statistics.md` | 短すぎる小見出し | 272 | `誤解①` | 誤解の内容まで見出しに含める（例: `### 誤解①：〇〇と混同しない`）。 |
| `pages/ds/japan-personal-information-protection-act.md` | 短すぎる小見出し | 167 | `### 誤解①  ` | 誤解の内容まで見出しに含める（例: `### 誤解①：〇〇と混同しない`）。 |
| `pages/ds/kernel.md` | 短すぎる小見出し | 180 | `誤解①` | 誤解の内容まで見出しに含める（例: `### 誤解①：〇〇と混同しない`）。 |
| `pages/ds/machine-learning-methods.md` | 短すぎる小見出し | 405 | `誤解①` | 誤解の内容まで見出しに含める（例: `### 誤解①：〇〇と混同しない`）。 |
| `pages/ds/missing-value-handling.md` | 短すぎる小見出し | 176 | `### 誤解①  ` | 誤解の内容まで見出しに含める（例: `### 誤解①：〇〇と混同しない`）。 |
| `pages/ds/nosql-datastore.md` | 短すぎる小見出し | 174 | `### 誤解①  ` | 誤解の内容まで見出しに含める（例: `### 誤解①：〇〇と混同しない`）。 |
| `pages/ds/personal-identifier-code.md` | 短すぎる小見出し | 145 | `### 誤解①  ` | 誤解の内容まで見出しに含める（例: `### 誤解①：〇〇と混同しない`）。 |
| `pages/ds/personally-related-information.md` | 短すぎる小見出し | 152 | `### 誤解①  ` | 誤解の内容まで見出しに含める（例: `### 誤解①：〇〇と混同しない`）。 |
| `pages/ds/pooling.md` | 短すぎる小見出し | 162 | `誤解①` | 誤解の内容まで見出しに含める（例: `### 誤解①：〇〇と混同しない`）。 |
| `pages/ds/pseudonymized-information.md` | 短すぎる小見出し | 144 | `### 誤解①  ` | 誤解の内容まで見出しに含める（例: `### 誤解①：〇〇と混同しない`）。 |
| `pages/ds/publickey-vs-symmetric.md` | 短すぎる小見出し | 206 | `誤解①` | 誤解の内容まで見出しに含める（例: `### 誤解①：〇〇と混同しない`）。 |
| `pages/ds/rdb-vs-nosql.md` | 短すぎる小見出し | 129 | `### 誤解①  ` | 誤解の内容まで見出しに含める（例: `### 誤解①：〇〇と混同しない`）。 |
| `pages/ds/sensitive-personal-information.md` | 短すぎる小見出し | 163 | `### 誤解①  ` | 誤解の内容まで見出しに含める（例: `### 誤解①：〇〇と混同しない`）。 |
| `pages/ds/third-party-provision.md` | 短すぎる小見出し | 182 | `### 誤解①  ` | 誤解の内容まで見出しに含める（例: `### 誤解①：〇〇と混同しない`）。 |
| `pages/ds/web-api.md` | 短すぎる小見出し | 218 | `誤解①` | 誤解の内容まで見出しに含める（例: `### 誤解①：〇〇と混同しない`）。 |

## 5. 手動フッター移行候補
次のDS記事では、本文中に `assign current_tags` / `for p in site.pages` / `count >= 5` などの手動関連記事ブロックが残っている。通常記事では `{% include ds_article_footer.html %}` への移行候補として別タスクで確認する。

<details>
<summary>手動フッター候補一覧（242件）</summary>

- `pages/ds/ai-utilization-skillcheck.md`
- `pages/ds/aiops-mlops-cheatsheet.md`
- `pages/ds/bcp.md`
- `pages/ds/bernoulli-binomial.md`
- `pages/ds/bi-operations-cheatsheet.md`
- `pages/ds/bi-tool-functions.md`
- `pages/ds/bias-variance-tradeoff.md`
- `pages/ds/binomial-bernoulli.md`
- `pages/ds/boxplot.md`
- `pages/ds/business-logic-and-data-importance.md`
- `pages/ds/business-skillcheck.md`
- `pages/ds/cap-theorem.md`
- `pages/ds/categorical-variable.md`
- `pages/ds/causal-inference.md`
- `pages/ds/ccpa.md`
- `pages/ds/chart-types.md`
- `pages/ds/chi-square-distribution.md`
- `pages/ds/cluster-analysis.md`
- `pages/ds/cnn.md`
- `pages/ds/coefficient-of-determination-contribution.md`
- `pages/ds/cognitive-bias.md`
- `pages/ds/compliance-risk.md`
- `pages/ds/confirmation-bias.md`
- `pages/ds/constructor.md`
- `pages/ds/contract-ukeoi-juninin.md`
- `pages/ds/convolution.md`
- `pages/ds/correlation-and-causation.md`
- `pages/ds/correlation-vs-causation.md`
- `pages/ds/covariance-and-correlation.md`
- `pages/ds/covariance-correlation.md`
- `pages/ds/cps-iot-digitaltwin-cheatsheet.md`
- `pages/ds/cps.md`
- `pages/ds/critical-path.md`
- `pages/ds/curse-of-dimensionality.md`
- `pages/ds/customer-journey.md`
- `pages/ds/data-ai-precautions.md`
- `pages/ds/data-augmentation.md`
- `pages/ds/data-driven-management.md`
- `pages/ds/data-driven.md`
- `pages/ds/data-extraction-vs-aggregation.md`
- `pages/ds/data-lake.md`
- `pages/ds/data-literacy-practice.md`
- `pages/ds/data-literacy.md`
- `pages/ds/data-mart.md`
- `pages/ds/data-transformation.md`
- `pages/ds/data-warehouse-vs-datamart.md`
- `pages/ds/database-constraints.md`
- `pages/ds/datalake-vs-nosql.md`
- `pages/ds/dependency-parsing.md`
- `pages/ds/design-of-experiments.md`
- `pages/ds/design-thinking.md`
- `pages/ds/deviation-score.md`
- `pages/ds/digital-image-representation.md`
- `pages/ds/digital-signature.md`
- `pages/ds/digital-signature2.md`
- `pages/ds/digital-twin.md`
- `pages/ds/discrete-continuous-distribution.md`
- `pages/ds/docker.md`
- `pages/ds/drilldown-drillup.md`
- `pages/ds/drillthrough.md`
- `pages/ds/dunning-kruger-effect.md`
- `pages/ds/e-calculus.md`
- `pages/ds/eda.md`
- `pages/ds/eigenvalue.md`
- `pages/ds/elsi.md`
- `pages/ds/encapsulation.md`
- `pages/ds/encoding.md`
- `pages/ds/engineering-skillcheck.md`
- `pages/ds/entropy.md`
- `pages/ds/er-diagram.md`
- `pages/ds/estimator-properties.md`
- `pages/ds/etl.md`
- `pages/ds/euclidean-norm.md`
- `pages/ds/evaluation-metrics-comparison.md`
- `pages/ds/evidence-based.md`
- `pages/ds/f-test.md`
- `pages/ds/feature-engineering.md`
- `pages/ds/feature-engineering2.md`
- `pages/ds/feature-importance.md`
- `pages/ds/file-transfer-protocol.md`
- `pages/ds/filter.md`
- `pages/ds/five-forces-analysis.md`
- `pages/ds/foreign-key.md`
- `pages/ds/gantt-chart.md`
- `pages/ds/gdpr.md`
- `pages/ds/gini-vs-entropy.md`
- `pages/ds/governance.md`
- `pages/ds/hadoop-vs-spark.md`
- `pages/ds/hadoop.md`
- `pages/ds/hallucination.md`
- `pages/ds/hash-function.md`
- `pages/ds/hash-vs-encryption.md`
- `pages/ds/hdfs.md`
- `pages/ds/hierarchical-clustering.md`
- `pages/ds/hierarchical-distance-metrics.md`
- `pages/ds/hot-cool-archive.md`
- `pages/ds/hypothesis-thinking.md`
- `pages/ds/iam-policy.md`
- `pages/ds/image-filter-processing.md`
- `pages/ds/image-metadata.md`
- `pages/ds/impurity.md`
- `pages/ds/imputation.md`
- `pages/ds/incident-management.md`
- `pages/ds/incremental-vs-differential-backup.md`
- `pages/ds/index.md`
- `pages/ds/industry4-0.md`
- `pages/ds/inheritance.md`
- `pages/ds/internal-control.md`
- `pages/ds/interpret-statistics.md`
- `pages/ds/inverse-matrix.md`
- `pages/ds/japan-personal-information-protection-act.md`
- `pages/ds/japanese-morphological-analysis-tools.md`
- `pages/ds/jupyter-r-usage.md`
- `pages/ds/kernel.md`
- `pages/ds/key-stretching.md`
- `pages/ds/kpi-kgi.md`
- `pages/ds/least-privilege.md`
- `pages/ds/left-join-where.md`
- `pages/ds/llm-temperature.md`
- `pages/ds/logistic-regression.md`
- `pages/ds/machine-learning-algorithms-cheatsheet.md`
- `pages/ds/machine-learning-methods.md`
- `pages/ds/malware.md`
- `pages/ds/managed-service.md`
- `pages/ds/mapping.md`
- `pages/ds/mapreduce.md`
- `pages/ds/matrix-multiplication.md`
- `pages/ds/mece.md`
- `pages/ds/metacognition.md`
- `pages/ds/mfa.md`
- `pages/ds/missing-value-handling.md`
- `pages/ds/ml-tasks.md`
- `pages/ds/mlops.md`
- `pages/ds/model-curriculum-summary.md`
- `pages/ds/nlp-cleaning.md`
- `pages/ds/nltk.md`
- `pages/ds/normal-and-standard-normal.md`
- `pages/ds/normalization-2nf-3nf.md`
- `pages/ds/nosql-datastore.md`
- `pages/ds/nosql.md`
- `pages/ds/oauth.md`
- `pages/ds/olap.md`
- `pages/ds/open-data.md`
- `pages/ds/operational-risk.md`
- `pages/ds/opt-out.md`
- `pages/ds/optional-math-algorithm.md`
- `pages/ds/outlier-visualization.md`
- `pages/ds/overfitting-tree-depth.md`
- `pages/ds/paired-vs-independent-data.md`
- `pages/ds/paper-structure.md`
- `pages/ds/pca.md`
- `pages/ds/pdca-cycle.md`
- `pages/ds/pearson-correlation.md`
- `pages/ds/personal-identifier-code.md`
- `pages/ds/personally-related-information.md`
- `pages/ds/pest-analysis.md`
- `pages/ds/pki.md`
- `pages/ds/poc-concept-proof.md`
- `pages/ds/point-interval-estimation.md`
- `pages/ds/polymorphism.md`
- `pages/ds/pooling.md`
- `pages/ds/population-sample-unbiased-variance.md`
- `pages/ds/power-law.md`
- `pages/ds/predictive-analytics.md`
- `pages/ds/preprocessing.md`
- `pages/ds/primary-key.md`
- `pages/ds/primary-secondary-data.md`
- `pages/ds/project-management.md`
- `pages/ds/pseudonymized-information.md`
- `pages/ds/publickey-vs-symmetric.md`
- `pages/ds/quartile.md`
- `pages/ds/rainbow-table-attack.md`
- `pages/ds/random-forest.md`
- `pages/ds/random-sampling-methods.md`
- `pages/ds/rbac.md`
- `pages/ds/rdb-vs-nosql.md`
- `pages/ds/referential-integrity.md`
- `pages/ds/regular-expression-basic.md`
- `pages/ds/regular-expression-date.md`
- `pages/ds/regular-expression-email.md`
- `pages/ds/regular-expression-postalcode.md`
- `pages/ds/regular-expression-summary.md`
- `pages/ds/replication-vs-backup.md`
- `pages/ds/report-line-risk-management.md`
- `pages/ds/reputation-risk.md`
- `pages/ds/rest-api-methods.md`
- `pages/ds/rest-api.md`
- `pages/ds/revenue-equation.md`
- `pages/ds/rfm-analysis.md`
- `pages/ds/risk-management.md`
- `pages/ds/rpo-rto.md`
- `pages/ds/sample-variance-unbiased-variance.md`
- `pages/ds/sampling-methods-comparison.md`
- `pages/ds/scrum.md`
- `pages/ds/self-join.md`
- `pages/ds/sensitive-personal-information.md`
- `pages/ds/sigmoid-function.md`
- `pages/ds/significance-level-and-pvalue.md`
- `pages/ds/skillcheck.md`
- `pages/ds/skilllevel-2023-assistant-ds-business.md`
- `pages/ds/skilllevel-2023-assistant-ds-dataengineering.md`
- `pages/ds/skilllevel-2023-assistant-ds-datascience.md`
- `pages/ds/skilllevel-2023-summary.md`
- `pages/ds/slice-dice.md`
- `pages/ds/soap.md`
- `pages/ds/social-data-ai-utilization.md`
- `pages/ds/society5.md`
- `pages/ds/sora-ame-kasa.md`
- `pages/ds/spark.md`
- `pages/ds/spearman-rank-correlation.md`
- `pages/ds/sql-count-diff.md`
- `pages/ds/sql-ddl-dml.md`
- `pages/ds/sql-exists.md`
- `pages/ds/sql-filtering.md`
- `pages/ds/sql-groupby.md`
- `pages/ds/sql-in-exists.md`
- `pages/ds/sql-join.md`
- `pages/ds/sql-union.md`
- `pages/ds/ssl-tls.md`
- `pages/ds/star-schema.md`
- `pages/ds/statistics-overview.md`
- `pages/ds/statistics-summary.md`
- `pages/ds/stemming-vs-lemmatization.md`
- `pages/ds/student-t-test.md`
- `pages/ds/swot-analysis.md`
- `pages/ds/symmetric-difference.md`
- `pages/ds/third-party-provision.md`
- `pages/ds/type1-type2-error.md`
- `pages/ds/variance-and-standard-deviation.md`
- `pages/ds/vector-dot-product.md`
- `pages/ds/visualization-basic-perspectives.md`
- `pages/ds/vpn-ssh.md`
- `pages/ds/wbs.md`
- `pages/ds/weak-strong-ai.md`
- `pages/ds/web-api.md`
- `pages/ds/web-crawling-scraping.md`
- `pages/ds/welch-t-test.md`
- `pages/ds/why-structure.md`
- `pages/ds/yarn.md`
- `pages/ds/z-score-method.md`
- `pages/ds/z-test.md`
- `pages/ds/zero-trust.md`

</details>

## 6. 推奨される次の対応順
1. まず、式や本文の意味が変わる真のレンダリング問題を修正する（例: `pages/ds/association-metrics.md` の分子説明H2化、本文中の `tags:` 行）。
2. 次に、`【対応スキル項目（...）】` を標準の `## 対応スキル項目（...）` へそろえる。
3. その後、水平線が多い記事の区切りを見出し中心に整理し、視覚ノイズを減らす。
4. 通常個別記事として残すページは、必要に応じてDS標準6見出しへ寄せる。ただし、比較記事・まとめ記事・索引ページは無理に合わせない。
5. 最後に、手動関連記事フッターを共有includeへ移行する。移行時は特殊構造の記事で表示が変わらないか個別確認する。

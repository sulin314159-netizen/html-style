# 纸墨编辑 · frontend-slides

来源：frontend-slides（用户采纳的 deck 工具；本卡对应它的 Paper & Ink 预设）
一句话：像一本印在好纸上的书——衬线、酒红、留白、页码；上台时安静但有分量。

## Tokens

```css
:root{
  --paper:#faf9f7;
  --ink:#1a1a1a;
  --muted:#6b645c;
  --accent:#c41e3a;      /* 酒红，唯一强调色 */
  --line:#ddd8cf;
  --white:#ffffff;
}
```

## 字体

- 展示/标题：`'Cormorant Garamond', 'Noto Serif SC', 'Songti SC', Georgia, serif`
- 正文：`'Source Serif 4', 'Noto Serif SC', Georgia, serif`
- **数字例外**：数据、页码、度量值一律用无衬线
  `'Inter', 'Segoe UI', system-ui, sans-serif`，并加
  `font-variant-numeric: lining-nums tabular-nums;`
- 中文正文 17–19px / 1.85；标题 60–120px，行高 0.95–1.1

## 版式

- 画布 1280×720 或 1920×1080；内边距 72×96（1280）或 100×120（1920）
- 封面：eyebrow（小字大写、字距 0.28em）→ 大标题 → 酒红斜体副标 → 一句引子 → 底部左右 meta
- 内页：eyebrow → 标题 → 一条 1px 发丝线 → 内容块
- 页码：右下 `01 / 05`，小字、字距 0.2em
- 只用 1px 线、留白、字号层级做分隔；**没有卡片、没有阴影、没有圆角**

## 内容密度（这是这个风格最容易翻车的地方）

- 每页至少三层：标题 / 一句支撑 / 信息块（3 列数字、3 行方法、或一段引文）
- 内容块的纵向位置用 `justify-content:center` 或 `space-between`，不要全部顶对齐再留一大片底白
- 一页放不下就拆页，不要把内容压成“标题 + 一排小字”

## 数字

- 酒红只给“结果值”，过程值用 `--ink`
- 所有数字用 lining 无衬线；**禁止用 Cormorant 渲染数据**（旧式数字会让 `1` 变成 `I`）
- 页面上出现 `12→1` 时，交付前确认读出来是“十二到一”，不是“I2 到 I”

## 文字密度

高。网页专栏 1000–2000 字正常；deck 每页 ≤ 100 字。文字是主角，但每页仍只讲一个观点。

## 网页模式

- 专栏/长文：单栏 65ch，纸底衬线，1px 发丝线分节
- 标题靠字号分层，不做卡片
- 数字仍用无衬线 lining

## deck 模式（原生）

- 1280×720 或 1920×1080；eyebrow + 大标题 + 发丝线
- 内容页三层；页码右下；键盘翻页
## 反模式

- 中文 drop cap（把“公”单独放大到 160px）
- 用 `❦ ☙ ✳` 当章节装饰（字体缺字会渲染成错位图案）
- 衬线数字
- 一页只有标题 + 三张小卡片，上下各空 40%
- 圆角卡片 / 阴影 / 渐变（那是 htmlppt-pitch，不是这一套）

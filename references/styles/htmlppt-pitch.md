# 柔和渐变 · htmlppt-pitch（deck）

来源：lewislulu/html-ppt-skill 的 pitch-deck 模板（用户采纳）
一句话：白底 + 渐变强调 + 圆角卡片，信息密度更高的商务 deck。

## Tokens

```css
:root{
  --bg:#ffffff;
  --bg-soft:#f6f7fb;
  --ink:#0d1130;
  --muted:#4a5070;
  --faint:#8a90ad;
  --border:rgba(20,25,60,.08);
  --accent:#3b5bff;
  --grad:linear-gradient(135deg, #3b5bff 0%, #7a46ff 55%, #d94cff 100%);
  --grad-soft:linear-gradient(135deg, #eef1ff, #f4edff 55%, #fbedff);
  --radius:20px;
  --radius-lg:28px;
  --shadow:0 14px 40px rgba(20,25,60,.08);
}
```

## 字号

- 封面标题 86px / 1.02，字重 900
- 内容标题 62px，字重 800
- 尾页 mega 180px
- 正文 17–19px / 1.75，`--muted`

## 版式

- 固定画布 1920×1080（或 1280×720），内边距 88–112px
- 卡片：白底 + `--shadow` + 圆角 20–28
- 渐变只用于：标题里的一个词、数字、小标签、尾页大字
- 内容页至少三层：kicker / 标题 / 卡片或 metrics

## 结构

1. Cover：左上品牌点 + kicker + 大标题 + 一句 lede + 底部页脚
2. Thesis：标题 + 3 张卡（每张一个论据）
3. Numbers：3 个 metric + 一句口径说明
4. Method：3 张卡（编号 + 标题 + 一句话）
5. Closing：mega 大字 + 一行副标 + pill

## 文字密度

中。每卡 1–2 句；deck 每页 ≤ 90 字。信息密度靠结构，不靠段落。

## 网页模式

- SaaS 落地页：白底、渐变强调、圆角卡片、三段式
- 渐变只给一个词/数字；卡片信息要有差

## deck 模式（原生）

- 1920×1080；白底 + 渐变词 + metric 卡
- 内容页至少三层；封面不要空一半
## 反模式

- 整页渐变背景
- 渐变文字超过两处
- 三张卡完全同构且没有信息差
- 页面上下各空一半（内容太扁）

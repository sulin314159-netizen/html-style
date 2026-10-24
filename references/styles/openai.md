# 黑白剧场 · openai

来源：openai.com/zh-Hans-CN（用户截图：黑底、大标题、彩色渐变素材块）
一句话：黑场 + 超大标题，让内容自己发光。

## Tokens

```css
:root{
  --bg:#000000;
  --surface:#111111;
  --surface-2:#1a1a1a;
  --text:#f5f5f5;
  --muted:rgba(255,255,255,.62);
  --line:rgba(255,255,255,.14);
  --white:#ffffff;
  --radius:14px;
  --radius-pill:999px;
}
```

## 字体

- `system-ui, -apple-system, "Segoe UI", "PingFang SC", sans-serif`
- 标题 clamp(56px, 8vw, 96px)，`letter-spacing:-.03em`，行高 1.0
- 正文 17–19px / 1.7，`--muted` 用于解释性文字

## 版式

- 全幅黑底，内容最大 1280px，左右 6vw
- 标题巨大、副文很短；每屏只留一个信息重心
- 卡片 = 素材块：彩色渐变 / 抽象图形 + 一行标题；不要白底卡片
- CTA：白色 pill 按钮，黑字

## 渐变素材（允许）

这是唯一允许出现彩色渐变的非 gradient 风格，但只用于**素材块/图片位**，不用于文字：

```css
background: radial-gradient(120% 120% at 20% 10%, #ff9a6b, #ff4d8d 45%, #7b5cff 100%);
```

## 动效

- 淡入 200ms；hover 提亮 2–4%
- 不做视差

## 适用 / 不适用

- 适用：品牌发布、深色落地页、产品大片
- 不适用：正式汇报投影（黑底易糊）、长文阅读、打印

## 文字密度

低。标题 + 一句副标 + 一个素材块；deck 每页 ≤ 40 字。字多了就不酷了。

## 网页模式

- 全幅黑底，内容 1280px；卡片=彩色素材块 + 一行标题
- 白色 pill CTA；不要白底卡片

## deck 模式

- 纯黑满屏；标题 `min(9vw,15vh)`；一页一句话
- 渐变素材只做视觉锚点（一处），不铺满
- 黑底投影容易糊：现场不可控时改用 moneyai / frontend-slides
## 反模式

- 白底 + 彩色卡片（那是 gradient / htmlppt）
- 渐变文字
- 圆角超过 16px 的大卡片

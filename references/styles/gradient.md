# 渐变梦幻 · gradient

来源：cn.goodpage.net + 114.55.169.242（同一族紫蓝渐变）
一句话：中文 SaaS 的安全牌——紫蓝渐变、白卡、柔光阴影。

## Tokens

```css
:root{
  --bg:#f8f9fa;
  --card:#ffffff;
  --text:#2c3e50;
  --muted:#7f8c8d;
  --primary:#667eea;
  --primary-2:#764ba2;
  --pink:#f093fb;
  --blue:#4facfe;
  --grad:linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  --grad-hero:linear-gradient(-45deg, #667eea, #764ba2, #f093fb, #4facfe);
  --radius:16px;
  --radius-lg:22px;
  --shadow:0 8px 24px rgba(102,126,234,.16);
  --shadow-lg:0 20px 50px rgba(102,126,234,.24);
}
```

## 字体

- `"PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif`
- 标题 600–700；正文 15–17px / 1.75

## 版式

- 容器 1100–1200px；区块间距 72–96px
- Hero 用 `--grad-hero`，白字；其余区块白底
- 卡片：白底、圆角 16–22、`--shadow`
- 强调只用渐变；不要再加第三个纯色强调

## 动效

- hover 上浮 2px + 阴影加深；180ms
- Hero 渐变可以缓慢流动（`background-size:200%`），但只一处

## 适用 / 不适用

- 适用：中文 SaaS、营销页、活动页、课程页
- 不适用：纪念/传记（太营销）、极简产品（太热闹）、深色场景

## 文字密度

中。每段 2–3 句；deck 每页 ≤ 80 字。卖点用短句，不要写成白皮书。

## 网页模式

- Hero 用 `--grad-hero`；其余白底；渐变不超过两处
- 卡片白底 + 柔光阴影；圆角 16–22

## deck 模式

- 白底为主；渐变只给标题里的一个词和数字
- 封面可以整块渐变，但全 deck 只此一页
- 别用渐变铺满内容页
## 反模式

- 渐变用在正文文字上
- 整页都是渐变背景
- 紫蓝渐变 + 玻璃拟态 + 大圆角同时出现（“AI 味”三件套）

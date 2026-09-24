# Domain Audit Rules

自定义节点审计域名与服务识别规则库。

## 规则格式

规则文件采用统一的 JSON 格式，保存在 `rules.json` 中：

```json
{
  "version": 1,
  "rules": [
    {
      "domain": "dotesports.com",
      "match": "suffix",
      "label": "游戏资讯"
    },
    {
      "domain": "api.example.com",
      "match": "exact",
      "label": "某应用"
    },
    {
      "domain": "192.0.2.0/24",
      "match": "cidr",
      "label": "示例服务网段"
    }
  ]
}
```

### 匹配模式说明

* `suffix`：后缀泛域名匹配（推荐用于主域名、整站分类）
* `exact`：完全精确匹配（用于特定 API 或独立用途的单点二级域）
* `cidr`：IP 网段匹配（用于特定基础设施或 CDN IP 网段）

## 自动化维护

本仓库规则库支持自动去重、格式校验及字母排序。

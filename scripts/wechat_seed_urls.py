#!/usr/bin/env python3
"""
Helper script to manually collect seed URLs from WeChat Pay documentation
Run this to find seed URLs for each major section
"""

# Known seed URLs (manually collected by navigating the site)
# To add more, visit https://pay.weixin.qq.com/doc/v3/merchant/4012062524
# Navigate to different sections and copy their URLs

SEED_URLS = {
    # 支付产品
    'JSAPI支付': [
        'https://pay.weixin.qq.com/doc/v3/merchant/4012062524',  # 产品介绍
        'https://pay.weixin.qq.com/doc/v3/merchant/4015423216',  # 快速开始
        'https://pay.weixin.qq.com/doc/v3/merchant/4012791870',  # 开发指引
    ],
    # Note: APP支付, H5支付, Native支付, 小程序支付, 合单支付 返回404
    # 仅保留有效的页面
    '付款码支付': [
        'https://pay.weixin.qq.com/doc/v3/merchant/4012647301',  # V2文档 (有效)
    ],
    '刷脸支付': [
        'https://pay.weixin.qq.com/doc/v3/merchant/4012647399',  # 有效
    ],

    # 运营工具
    # Note: 商家转账, 微信支付分的某些页面返回404
    # 代金券, 商家券的初始页面返回404
    '现金红包': [
        'https://pay.weixin.qq.com/doc/v3/merchant/4012647471',  # V2文档 (有效)
    ],

    # 扩展工具
    # Note: 分账, 消费者投诉的初始页面返回404
    '清关报关': [
        'https://pay.weixin.qq.com/doc/v3/merchant/4012647500',  # V2文档 (有效)
    ],

    # 通用规则
    '通用规则': [
        'https://pay.weixin.qq.com/doc/v3/merchant/4012081606',  # APIv3概述
        'https://pay.weixin.qq.com/doc/v3/merchant/4012068443',  # 接入模式
    ],

    # SDK和开发工具
    'SDK和开发工具': [
        'https://pay.weixin.qq.com/doc/v3/merchant/4012076498',  # SDK下载
    ],
}

def generate_root_urls_list():
    """Generate a flat list of all seed URLs"""
    all_urls = []
    for category, urls in SEED_URLS.items():
        all_urls.extend(urls)
    return all_urls

def print_python_list():
    """Print as Python list for easy copy-paste"""
    urls = generate_root_urls_list()
    print("# Paste this into 10_discover_wechat_pay.py:")
    print("\nROOT_URLS = [")
    for url in urls:
        print(f"    '{url}',")
    print("]")
    print(f"\n# Total seed URLs: {len(urls)}")

if __name__ == '__main__':
    print("WeChat Pay Documentation Seed URLs")
    print("=" * 60)
    print("\nNOTE: These are manually collected seed URLs.")
    print("To discover ALL documentation, you need to manually navigate")
    print("to each collapsed section and add at least one URL from it.\n")

    print_python_list()

    print("\n" + "=" * 60)
    print("How to add more seed URLs:")
    print("1. Visit https://pay.weixin.qq.com/doc/v3/merchant/4012062524")
    print("2. Click on collapsed sections in the sidebar")
    print("3. Copy the URL of any page in that section")
    print("4. Add it to the SEED_URLS dict above")
    print("=" * 60)

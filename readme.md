##预先收集免费代理ip的网站信息
#name---网站标识名
#url_t---请求目标网站第一部分（由三部分组成）
#url_d---请求目标网站第三部分
#page---爬取的页数
#xpath---爬取数据的行数的xpath（一般是table的tr）
#xpath_ip---爬取ip的xpath
#xpath_port---爬取端口的
#xpath_type---爬取代理类型（http/https）的xpath
#xpath_country---爬取代理的地区的xpath
#xpath_anonymous---爬取代理的匿名性的xpath

{
        "name": "kuaida",
        "url_t": "https://www.kuaidaili.com/free/inha/",
        "url_d": "/",
        "pages": "4",
        "xpath": "//table/tbody/tr",
        "xpath_ip": "td[1]/text()",
        "xpath_port": "td[2]/text()",
        "xpath_type": "td[4]/text()",
        "xpath_country": "td[5]/text()",
        "xpath_anonymous": "td[3]/text()"
    }

# -*- coding: utf-8 -*-
import scrapy,json
from ..spiders.traffic import Get_traffic
from ..spiders.write_city import write_scenic,write_city


class XiechengappSpider(scrapy.Spider):
    name = 'xiechengapp'
    allowed_domains = ['you.ctrip.com']
    start_urls = ['https://you.ctrip.com/sitelist/china110000.html']

    def parse(self, response):
        # 首先先把热门城市内容获取完之后在获取普通城市...
        hot_ul = response.xpath('//div[@class="hot_destlist cf"]/ul/li')
        for note in hot_ul:
            info_city = {}
            # 获取城市
            info_city['city'] = note.xpath('.//a/div/dl/dt/text()').extract_first()
            # 获取城市id
            info_city['city_id'] = note.xpath('.//a/@href').extract_first().split('/')[2].split('.')[0]
            info_city['city_num'] = ''
            write_city(info_city)

            # 拼接景点列表url
            url = 'https://you.ctrip.com/sight/{}'.format(info_city['city_id'])
            base_url = url + '/s0-p1.html#sightname'
            # 　调用获取景点列表
            yield scrapy.Request(base_url, callback=self.Get_List, meta=info_city)

            # # 提取每个城市的前10页
            # for page in range(1, 11):
            #     base_url = url + '/s0-p{}.html#sightname'.format(page)
            #     # 　调用获取景点列表
            #     yield scrapy.Request(base_url, callback=self.Get_List, meta=info_city)

        # 获取普通城市
        ul = response.xpath('//ul[@class="c_city_nlist cf"]/li')
        for li in ul:
            info_city = {}
            info_city['city_num'] = '150'
            # 获取城市
            info_city['city'] = li.xpath('.//a/text()').extract_first()
            # 获取城市id
            info_city['city_id'] = li.xpath('.//a/@href').extract_first().split('/')[2].split('.')[0]

            write_city(info_city)

            # 拼接景点列表url
            url = 'https://you.ctrip.com/sight/{}'.format(info_city['city_id'])
            base_url = url + '/s0-p1.html#sightname'
            # 　调用获取景点列表
            yield scrapy.Request(base_url, callback=self.Get_List, meta=info_city)

            # # 提取每个城市的前10页
            # for page in range(1, 11):
            #     base_url = url + '/s0-p{}.html#sightname'.format(page)
            #     # 　调用获取景点列表
            #     yield scrapy.Request(base_url, callback=self.Get_List)

    '''
         景点  获取景点id 获取评分 评论条数 排名 景点地区 等级  电话   开放时间    介绍       景色得分      趣味得分        性价比得分
       scenic scenic_id branch comment rank local grade phone come_time introduce scenic_score interest_score cost_score
        
        情路出游   家庭亲子     朋友出游   商务旅行   单独旅行       很好        好         一般        差          很差          交通
        feel_cmt family_cmt friend_cmt shop_cmt alone_cmt very_good_cmt good_cmt commonly_cmt wrong_cmt very_wrong_cmt  traffic
           
    '''

    # 获取景点列表
    def Get_List(self, response):
        infos = {}
        div_list = response.xpath('//div[@class="list_wide_mod2"]/div')
        for div_li in div_list:

            # 获取景点
            scenic = div_li.xpath('.//div/dl/dt/a/text()').extract_first()
            if scenic:
                infos['scenic'] = div_li.xpath('.//div/dl/dt/a/text()').extract_first()
                # 获取景点id
                infos['scenic_id'] = div_li.xpath('.//div/a/@href').extract_first().split('/')[3].split('.')[0]
                # 获取评分
                infos['branch'] = div_li.xpath('.//ul[@class="r_comment"]/li/a/strong/text()').extract_first()
                # 获取评论条数
                infos['comment'] = div_li.xpath('.//ul[@class="r_comment"]/li[3]/a/text()').extract_first().replace('\n',
                                                                                                                   '').replace(
                    ' ', '')
                # 获取排名有则赋值,无则返回None
                infos['rank'] = div_li.xpath('.//div[@class="rdetailbox"]/dl/dt/s/text()').extract_first()
                # 获取景点地区
                infos['local'] = div_li.xpath('.//div[@class="rdetailbox"]/dl/dd/text()').extract_first().replace('\n',
                                                                                                                 '').replace(
                    ' ', '')

                # 拼接完整url进入详情
                url = response.url.split('/')[5]
                bases_url = response.url.replace(url, infos['scenic_id']) + '.html' + '#sightname'

                # 调用详情页
                yield scrapy.Request(bases_url, callback=self.Get_Data,meta={'infos':infos})

    # 获取详情数据
    def Get_Data(self, response):

        infos = response.meta['infos']
        # print(infos['scenic'])
        # 等级
        grade = response.xpath('//ul[@class="s_sight_in_list"]/li[1]/span[@class="s_sight_con"]/text()')
        if len(grade) <= 0:
            infos['grade'] = 'None'
        else:
            infos['grade'] = response.xpath(
                '//ul[@class="s_sight_in_list"]/li[1]/span[@class="s_sight_con"]/text()').extract_first().replace('\n',
                                                                                                                  '').replace(
                ' ', '')

        # 电话
        phone = response.xpath('//ul[@class="s_sight_in_list"]/li[2]/span[@class="s_sight_con"]/text()')
        if len(phone) <= 0:
            infos['phone'] = 'None'
        else:
            infos['phone'] = response.xpath(
                '//ul[@class="s_sight_in_list"]/li[2]/span[@class="s_sight_con"]/text()').extract_first().replace('\n',
                                                                                                                  '').replace(
                ' ', '')

        # 开放时间
        come_time = response.xpath('//dl[@class="s_sight_in_list"]/dd/text()')
        if len(come_time) <= 0:
            infos['come_time'] = 'None'
        else:
            infos['come_time'] = response.xpath('//dl[@class="s_sight_in_list"]/dd/text()').extract_first()

        # 介绍
        introduce = response.xpath('//div[@class="text_style"]/p/text()')
        if len(introduce) <= 0:
            infos['introduce'] = 'None'
        else:
            infos['introduce'] = response.xpath('//div[@class="text_style"]/p/text()').extract_first()

        # 景色得分
        scenic_score = response.xpath('//dl[@class="comment_show"]/dd[1]/span[@class="score"]/text()')
        if len(scenic_score) <= 0:
            infos['scenic_score'] = 'None'
        else:
            infos['scenic_score'] = response.xpath(
                '//dl[@class="comment_show"]/dd[1]/span[@class="score"]/text()').extract_first()

        # 趣味得分
        interest_score = response.xpath('//dl[@class="comment_show"]/dd[2]/span[@class="score"]/text()')
        if len(interest_score) <= 0:
            infos['interest_score'] = 'None'
        else:
            infos['interest_score'] = response.xpath(
                '//dl[@class="comment_show"]/dd[2]/span[@class="score"]/text()').extract_first()

        # 性价比得分
        cost_score = response.xpath('//dl[@class="comment_show"]/dd[3]/span[@class="score"]/text()')
        if len(cost_score) <= 0:
            infos['cost_score'] = 'None'
        else:
            infos['cost_score'] = response.xpath(
                '//dl[@class="comment_show"]/dd[3]/span[@class="score"]/text()').extract_first()

        # 评论条数(情路出游)
        feel_cmt = response.xpath('//ul[@class="cate_count"]/li[1]/a/span[@class="ct_count"]/text()')
        if len(feel_cmt) <= 0:
            infos['feel_cmt'] = 'None'
        else:
            infos['feel_cmt'] = response.xpath(
                '//ul[@class="cate_count"]/li[1]/a/span[@class="ct_count"]/text()').extract_first()

        # 评论条数(家庭亲子)
        family_cmt = response.xpath('//ul[@class="cate_count"]/li[2]/a/span[@class="ct_count"]/text()')
        if len(family_cmt) <= 0:
            infos['family_cmt'] = 'None'
        else:
            infos['family_cmt'] = response.xpath(
                '//ul[@class="cate_count"]/li[2]/a/span[@class="ct_count"]/text()').extract_first()

        # 评论条数(朋友出游)
        friend_cmt = response.xpath('//ul[@class="cate_count"]/li[2]/a/span[@class="ct_count"]/text()')
        if len(friend_cmt) <= 0:
            infos['friend_cmt'] = 'None'
        else:
            infos['friend_cmt'] = response.xpath(
                '//ul[@class="cate_count"]/li[2]/a/span[@class="ct_count"]/text()').extract_first()

        # 评论条数(商务旅行)
        shop_cmt = response.xpath('//ul[@class="cate_count"]/li[2]/a/span[@class="ct_count"]/text()')
        if len(shop_cmt) <= 0:
            infos['shop_cmt'] = 'None'
        else:
            infos['shop_cmt'] = response.xpath(
                '//ul[@class="cate_count"]/li[2]/a/span[@class="ct_count"]/text()').extract_first()

        # 评论条数(单独旅行)
        alone_cmt = response.xpath('//ul[@class="cate_count"]/li[2]/a/span[@class="ct_count"]/text()')
        if len(alone_cmt) <= 0:
            infos['alone_cmt'] = 'None'
        else:
            infos['alone_cmt'] = response.xpath(
                '//ul[@class="cate_count"]/li[2]/a/span[@class="ct_count"]/text()').extract_first()

        # 评论条数(很好)
        very_good_cmt = response.xpath('//div[@class="detailtab cf"]/ul/li[2]/a/span/text()')
        if len(very_good_cmt) <= 0:
            infos['very_good_cmt'] = 'None'
        else:
            infos['very_good_cmt'] = response.xpath(
                '//ul[@class="cate_count"]/li[2]/a/span[@class="ct_count"]/text()').extract_first()

        # 评论条数(好)
        good_cmt = response.xpath('//div[@class="detailtab cf"]/ul/li[3]/a/span/text()')
        if len(good_cmt) <= 0:
            infos['good_cmt'] = 'None'
        else:
            infos['good_cmt'] = response.xpath('//div[@class="detailtab cf"]/ul/li[3]/a/span/text()').extract_first()

        # 评论条数(一般)
        commonly_cmt = response.xpath('//div[@class="detailtab cf"]/ul/li[4]/a/span/text()')
        if len(commonly_cmt) <= 0:
            infos['commonly_cmt'] = 'None'
        else:
            infos['commonly_cmt'] = response.xpath('//div[@class="detailtab cf"]/ul/li[4]/a/span/text()').extract_first()

        # 评论条数(差)
        wrong_cmt = response.xpath('//div[@class="detailtab cf"]/ul/li[5]/a/span/text()')
        if len(wrong_cmt) <= 0:
            infos['wrong_cmt'] = 'None'
        else:
            infos['wrong_cmt'] = response.xpath('//div[@class="detailtab cf"]/ul/li[5]/a/span/text()').extract_first()

        # 评论条数(很差)
        very_wrong_cmt = response.xpath('//div[@class="detailtab cf"]/ul/li[6]/a/span/text()')
        if len(very_wrong_cmt) <= 0:
            infos['very_wrong_cmt'] = 'None'
        else:
            infos['very_wrong_cmt'] = response.xpath(
                '//div[@class="detailtab cf"]/ul/li[6]/a/span/text()').extract_first()

        # 调用traffic模块调出其中的交通详情
        url = response.url.replace('.html', '-traffic.html#jiaotong')
        infos['traffic'] = Get_traffic(url)

        # print(infos)
        # # write_scenic(infos)
        with open('scenic.json', 'a+') as f:
            f.write(json.dumps(infos, ensure_ascii=False) + '\n')
            f.close()

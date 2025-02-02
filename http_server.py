from flask import Flask, request, Response
from json import dumps

import utils

app = Flask(__name__)
app.debug = True
localIp = utils.get_ip_addr()
retResult = [
    {
        "id": 0,
        "title": "beyond-大地",
        "desc": "港颁奖 表述了父爱的伟大 父亲胸襟的宽广 与对父亲的想念 回忆过去在异乡的感觉",
        "playUrl": "https://user-images.githubusercontent.com/20841967/233770339-e9962ea2-436b-4c85-83f4-f80321015f20.mp4",
        "authorName": "beyond",
        "imageUrl": "https://p6-pc-sign.douyinpic.com/tos-cn-p-0015/a819fbde8dae41b4b95a59562aa38a54~tplv-dy-resize-origshort-autoq-75:330.jpeg?biz_tag=pcweb_cover&from=3213915784&s=PackSourceEnum_AWEME_DETAIL&sc=cover&se=false&x-expires=1996239600&x-signature=oRQX6rJDjuxgKQRt6Jl7vtKv3Sk%3D",
        "collectionCount": "24"
    },
    {
        "id": 0,
        "title": "脆皮炸鲜奶",
        "desc": "无敌香甜美味 # 美食 # 甜点……",
        "playUrl": "https://user-images.githubusercontent.com/20841967/233770382-1f9fee7f-d418-4a27-9785-98c36eca143f.mp4",
        "authorName": "甜点",
        "imageUrl": "https://p9-pc-sign.douyinpic.com/tos-cn-p-0015/f5de5023134848e99a0b455b0d2a7f47~tplv-dy-resize-origshort-autoq-75:330.jpeg?biz_tag=pcweb_cover&from=3213915784&s=PackSourceEnum_AWEME_DETAIL&sc=cover&se=false&x-expires=1996239600&x-signature=QCNywvpquxzT%2FlCUIPivcgbLnyE%3D",
        "collectionCount": "99"
    },
    {
        "id": 0,
        "title": "科比-篮球",
        "desc": "科比的投篮就像一门艺术，美到极致，便成艺术。# 篮球偶像 # 赛事",
        "authorName": "篮球",
        "playUrl": "https://user-images.githubusercontent.com/20841967/233770462-88ce1e3c-f1bd-47de-92e1-b4dff5818ecb.mp4",
        "imageUrl": "https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fsafe-img.xhscdn.com%2Fbw1%2Fb989ab69-d5dd-419a-bce8-f808d8c4b809%3FimageView2%2F2%2Fw%2F1080%2Fformat%2Fjpg&refer=http%3A%2F%2Fsafe-img.xhscdn.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1683472723&t=2b7371a869dbb4d6fdd8bb2e97aec30d",
        "collectionCount": "66"
    },
    {
        "id": 0,
        "title": "梵净山",
        "desc": "自然的鬼斧神工，加上故人的智慧，500年前建造而成... # 景色 # 奇观",
        "authorName": "梵净山",
        "playUrl": "https://user-images.githubusercontent.com/20841967/233770663-7a322b0d-43e4-4a86-86d1-57af50687e02.mp4",
        "imageUrl": "https://p6-pc-sign.douyinpic.com/image-cut-tos-priv/c08da21ddbd078d3f22ebb4994f10b87~tplv-dy-resize-origshort-autoq-75:330.jpeg?biz_tag=pcweb_cover&from=3213915784&s=PackSourceEnum_MIX_AWEME&sc=cover&se=false&x-expires=1996239600&x-signature=rngb42bP69sVeXVeymC76%2FVVIGQ%3D",
        "collectionCount": "10"
    },
    {
        "id": 0,
        "title": "最爱 完整版",
        "desc": "汐退和涨 月冷风和霜 夜雨的狂想 野花的微香 # 经典歌曲 # 粤语",
        "authorName": "KTV麦霸",
        "playUrl": "https://vdn1.vzuu.com/HD/c8af2fd6-438d-11eb-991f-da1190f1515e.mp4",
        "imageUrl": "https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fpic4.zhimg.com%2Fv2-36249b426ad7f246d14d51f8a9844016_1440w.jpg&refer=http%3A%2F%2Fpic4.zhimg.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1661767737&t=dfe5a7a908164f771dca7c33958f5302",
        "collectionCount": "18"
    },
    {
        "id": 0,
        "title": "利昂内尔·梅西",
        "desc": "西经典时刻 # 阿根廷球队 # 足球 # 赛事",
        "authorName": "利昂内尔·梅西",
        "playUrl": "https://cdn.singsingenglish.com/new-sing/66c3d05eaa177e07d57465f948f0d8b934b7a7ba.mp4",
        "imageUrl": "https://p9-pc-sign.douyinpic.com/tos-cn-i-dy/ia12e0af1a929401b9d3387a1bff89a46~tplv-dy-resize-origshort-autoq-75:330.jpeg?biz_tag=pcweb_cover&from=3213915784&s=PackSourceEnum_WEBPC_RELATED_AWEME&sc=cover&se=false&x-expires=1682089200&x-signature=%2Bicaky%2BVfQbQgIFyoB%2FbyPIXdK0%3D",
        "collectionCount": "10"
    },
    {
        "id": 0,
        "title": "樱木花道和赤木晴子",
        "desc": "典再现荧屏，灌篮高手中樱木花道的超燃高光时刻! # 动漫 # 灌篮高手",
        "authorName": "灌篮高手",
        "playUrl": "https://user-images.githubusercontent.com/20841967/233770686-99285e55-9caa-49ad-b1ac-59d7d6cc223f.mp4",
        "imageUrl": "https://gimg2.baidu.com/image_search/src=http%3A%2F%2Finews.gtimg.com%2Fnewsapp_bt%2F0%2F11464763925%2F1000.jpg&refer=http%3A%2F%2Finews.gtimg.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1661749867&t=024e12db91dff8d30febc6581b36407b",
        "collectionCount": "99"
    },
    {
        "id": 0,
        "title": "霍尔比特人-五军之战",
        "desc": "环王经典战斗场面，圣光降临，魔戒超燃战斗场面# 超燃 # 科幻# 视觉震撼 #..",
        "authorName": "指环王",
        "playUrl": "https://storage.googleapis.com/exoplayer-test-media-1/mkv/android-screens-lavf-56.36.100-aac-avc-main-1280x720.mkv",
        "imageUrl": "https://p6-pc-sign.douyinpic.com/image-cut-tos-priv/741aa3bbeca63b5de16419c92b77cc83~tplv-dy-resize-origshort-autoq-75:330.jpeg?biz_tag=pcweb_cover&from=3213915784&s=PackSourceEnum_AWEME_DETAIL&sc=cover&se=false&x-expires=1996228800&x-signature=bFriYl2mN5IWIsJyFpNupTFoFRo%3D",
        "collectionCount": "42"
    },
    {
        "id": 0,
        "title": "风云2-万剑归宗",
        "desc": "效天花板，武林会战",
        "authorName": "风云",
        "playUrl": "https://user-images.githubusercontent.com/20841967/233770736-313f3016-2993-4864-af35-2f13390c3221.mp4",
        "imageUrl": "https://p3-pc-sign.douyinpic.com/image-cut-tos-priv/c9b374cd867bc34a651568390033c3b9~tplv-dy-resize-origshort-autoq-75:330.jpeg?biz_tag=pcweb_cover&from=3213915784&s=PackSourceEnum_AWEME_DETAIL&sc=cover&se=false&x-expires=1996225200&x-signature=hrZGi%2FNu8fbiDLkswRR9x6W7zcg%3D",
        "collectionCount": "48"
    },
    {
        "id": 0,
        "title": "千与千寻",
        "desc": "经典动漫，回味无穷 # 宫崎骏",
        "authorName": "宫崎骏",
        "playUrl": "https://user-images.githubusercontent.com/20841967/233770768-2ec5d79a-bd10-4430-bbe9-24aabbe971c8.mp4",
        "imageUrl": "https://gss0.baidu.com/-fo3dSag_xI4khGko9WTAnF6hhy/zhidao/pic/item/0823dd54564e9258cf1436509d82d158ccbf4e6f.jpg",
        "collectionCount": "86"
    },
    {
        "id": 0,
        "title": "最正宗的龟派气功波",
        "desc": "正宗的龟派气功波# 七龙珠 # 怀旧动画 # 孙悟空",
        "authorName": "七龙珠",
        "playUrl": "https://user-images.githubusercontent.com/20841967/233770791-61684fbb-3360-434c-9da1-eb7ad71f7b22.mp4",
        "imageUrl": "https://inews.gtimg.com/newsapp_bt/0/13794563706/641",
        "collectionCount": "22"
    },
    {
        "id": 0,
        "title": "马超大战曹操",
        "desc": "马超率二十万大军攻打曹操，势如破竹，曹操割须断袍",
        "authorName": "新三国",
        "playUrl": "https://user-images.githubusercontent.com/20841967/233770819-e8b1e666-7635-48d7-9efa-04c5ceb06ee3.mp4",
        "imageUrl": "https://p3-sign.bdxiguaimg.com/tos-cn-i-0004/30fe62edb0ee444080b6832809f79912~tplv-pk90l89vgd-crop-center:864:486.jpeg?x-expires=1712405343&x-signature=DAYhI08fI51PlN2J6Ygk%2B%2BJrF9o%3D",
        "collectionCount": "66"
    }
]


@app.route(rule='/list', methods=['POST', 'GET'])
def get_list():
    print("get request from client,", request.method)
    if request.method == 'POST':
        key = request.form.get('key', default='')
        page = request.form.get('page', default='')
        response = {'code': 200, 'msg': 'success', 'data': retResult}
        return Response(dumps(response), mimetype='application/json')

    elif request.method == 'GET':
        key = request.args.get('key', default='')
        page = request.args.get('page', default='')
        if key is None:
            key = ''
        if page is None:
            page = ''
        response = {'code': 200, 'msg': 'success', 'data': retResult}
        return Response(dumps(response), mimetype='application/json')


if __name__ == '__main__':
    app.run(host=localIp, port=6789, debug=False)

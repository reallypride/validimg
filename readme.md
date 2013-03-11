# ValidImg #
Python验证码，使用不同的颜色区分，有别于传统的验证码，更加安全。

## 例子： ##

----------

> from validimg import ValidImage

> vi = ValidImage(120, 60)

> vi.set_font_file('/home/www/fonts/msyh.ttf')

> buf_str, s = vi.draw_text(u'我是中国人')

> response = HttpResponse(buf_str, content_type='image/jpeg')

> return response

![](http://www.ifishblog.com/validimg/20130311215213.png)


----------


> from validimg import ValidImage

> vi = ValidImage(120, 60)

> buf_str, s = vi.draw_number()

> response = HttpResponse(buf_str, content_type='image/jpeg')

> return response

![](http://www.ifishblog.com/validimg/20130311220102.png)
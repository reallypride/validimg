import Image, ImageDraw, ImageFont
import random
import StringIO

class ValidImage(object):
    
    def __init__(self, width, height, color='#111111'):
        self.width = width
        self.height = height
        self.bgcolor = color
        self.font_file = '/usr/share/fonts/truetype/ttf-dejavu/DejaVuSansMono.ttf'
        
    def draw_number(self, num=6, font_size=18, color='#FF0000'):
        numbers = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
        rnums = random.sample(numbers, num)
        font = ImageFont.truetype(self.font_file, font_size)

        twidth, theight = font.getsize(''.join(rnums))
        swidth = (self.width - twidth - 10) / 2
        sheight = (self.height - theight) / 2
        rindex = random.randint(0, num/2)
        
        img = Image.new('RGB', (self.width, self.height), self.bgcolor)
        draw = ImageDraw.Draw(img)
        
        if rindex:
            s1 = ''.join(rnums[0:rindex])
            draw.text((swidth, sheight), s1, font=font)
            swidth += font.getsize(s1)[0] + 5
            
        s2 = ''.join(rnums[rindex:rindex+num/2])
        draw.text((swidth, sheight), s2, font=font, fill=color)
        
        swidth += font.getsize(s2)[0] + 5
        s3 = ''.join(rnums[rindex+num/2:])
        if s3:
            draw.text((swidth, sheight), s3, font=font)
        
        buf = StringIO.StringIO()
        img.save(buf, 'jpeg')
        buf_str = buf.getvalue()
        buf.close()
    
        return buf_str, s2
    
    def draw_text(self, text, num=2, font_size=18, color='#FF0000'):
        font = ImageFont.truetype(self.font_file, font_size)

        twidth, theight = font.getsize(text)
        swidth = (self.width - twidth - 10) / 2
        sheight = (self.height - theight) / 2
        rindex = random.randint(0, len(text) - num)
        
        img = Image.new('RGB', (self.width, self.height), self.bgcolor)
        draw = ImageDraw.Draw(img)
        
        if rindex:
            s1 = text[0:rindex]
            draw.text((swidth, sheight), s1, font=font)
            swidth += font.getsize(s1)[0] + 5
        
        s2 = text[rindex:rindex+num]
        draw.text((swidth, sheight), s2, font=font, fill=color)
        
        swidth += font.getsize(s2)[0] + 5
        s3 = text[rindex+num:]
        if s3:
            draw.text((swidth, sheight), s3, font=font)
        
        buf = StringIO.StringIO()
        img.save(buf, 'jpeg')
        buf_str = buf.getvalue()
        buf.close()
    
        return buf_str, s2
    
    def set_font_file(self, filename):
        self.font_file = filename
        
from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):
    def start_element(self,name,attrs):
        print('sax:start_element:%s,attrs:%s'%(name,str(attrs)))
    
    def end_element(self,name):
        print('sax:end_element:%s'%name)

    def char_data(self,text):
        print('sax:char_data:%s'%text)

xml=r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler=DefaultSaxHandler()
parser=ParserCreate()
parser.StartElementHandler=handler.start_element
parser.EndElementHandler=handler.end_element
parser.CharacterDataHandler=handler.char_data
parser.Parse(xml)


class WeatherSaxHandler(object):
    def __init__(self):  
        self.weather_data = {}
        self.date_index = 0
    def start_element(self, name, attrs):
        if name=="yweather:location":
            self.weather_data['city'] = attrs['city']
            self.weather_data['country'] = attrs['country']
        if name=="yweather:forecast" and self.date_index<2:
            if self.date_index==0:
                self.weather_data['today'] = {}
                self.weather_data['today']['text'] = attrs['text']
                self.weather_data['today']['low'] = int(attrs['low'])
                self.weather_data['today']['high'] = int(attrs['high'])
                self.date_index += 1
            elif self.date_index==1:
                self.weather_data['tomorrow'] = {}
                self.weather_data['tomorrow']['text'] = attrs['text']
                self.weather_data['tomorrow']['low'] = int(attrs['low'])
                self.weather_data['tomorrow']['high'] = int(attrs['high'])
                self.date_index += 1
    def end_element(self, name):
        pass

    def char_data(self, text):
        pass

def parse_weather(xml):
    handler = WeatherSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(xml)
    return handler.weather_data

data=r'''<?xml version="1.0" encoding="UTF-8"?>
<query xmlns:yahoo="http://www.yahooapis.com/v1/base.rng"
    yahoo:count="1" yahoo:created="2017-03-13T15:58:23Z" yahoo:lang="zh-CN">
    <results>
        <channel>
            <yweather:units
                xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0"
                distance="mi" pressure="in" speed="mph" temperature="F"/>
            <title>Yahoo! Weather - Dongguan, Guangdong, CN</title>
            <link>http://us.rd.yahoo.com/dailynews/rss/weather/Country__Country/*https://weather.yahoo.com/country/state/city-2161842/</link>
            <description>Yahoo! Weather for Dongguan, Guangdong, CN</description>
            <language>en-us</language>
            <lastBuildDate>Mon, 13 Mar 2017 11:58 PM CST</lastBuildDate>
            <ttl>60</ttl>
            <yweather:location
                xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0"
                city="Dongguan" country="China" region=" Guangdong"/>
            <yweather:wind
                xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0"
                chill="72" direction="180" speed="11"/>
            <yweather:atmosphere
                xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0"
                humidity="94" pressure="1011.0" rising="0" visibility="11.2"/>
            <yweather:astronomy
                xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0"
                sunrise="6:36 am" sunset="6:34 pm"/>
            <image>
                <title>Yahoo! Weather</title>
                <width>142</width>
                <height>18</height>
                <link>http://weather.yahoo.com</link>
                <url>http://l.yimg.com/a/i/brand/purplelogo//uh/us/news-wea.gif</url>
            </image>
            <item>
                <title>Conditions for Dongguan, Guangdong, CN at 11:00 PM CST</title>
                <geo:lat xmlns:geo="http://www.w3.org/2003/01/geo/wgs84_pos#">23.046499</geo:lat>
                <geo:long xmlns:geo="http://www.w3.org/2003/01/geo/wgs84_pos#">113.735817</geo:long>
                <link>http://us.rd.yahoo.com/dailynews/rss/weather/Country__Country/*https://weather.yahoo.com/country/state/city-2161842/</link>
                <pubDate>Mon, 13 Mar 2017 11:00 PM CST</pubDate>
                <yweather:condition
                    xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0"
                    code="29" date="Mon, 13 Mar 2017 11:00 PM CST"
                    temp="71" text="Partly Cloudy"/>
                <yweather:forecast
                    xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0"
                    code="30" date="13 Mar 2017" day="Mon" high="77"
                    low="66" text="Partly Cloudy"/>
                <yweather:forecast
                    xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0"
                    code="39" date="14 Mar 2017" day="Tue" high="73"
                    low="61" text="Scattered Showers"/>
                <yweather:forecast
                    xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0"
                    code="26" date="15 Mar 2017" day="Wed" high="69"
                    low="59" text="Cloudy"/>
                <yweather:forecast
                    xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0"
                    code="26" date="16 Mar 2017" day="Thu" high="67"
                    low="60" text="Cloudy"/>
                <yweather:forecast
                    xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0"
                    code="28" date="17 Mar 2017" day="Fri" high="72"
                    low="63" text="Mostly Cloudy"/>
                <yweather:forecast
                    xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0"
                    code="28" date="18 Mar 2017" day="Sat" high="74"
                    low="65" text="Mostly Cloudy"/>
                <yweather:forecast
                    xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0"
                    code="39" date="19 Mar 2017" day="Sun" high="72"
                    low="66" text="Scattered Showers"/>
                <yweather:forecast
                    xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0"
                    code="39" date="20 Mar 2017" day="Mon" high="73"
                    low="67" text="Scattered Showers"/>
                <yweather:forecast
                    xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0"
                    code="12" date="21 Mar 2017" day="Tue" high="74"
                    low="68" text="Rain"/>
                <yweather:forecast
                    xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0"
                    code="30" date="22 Mar 2017" day="Wed" high="75"
                    low="68" text="Partly Cloudy"/>
                <description>&lt;![CDATA[&lt;img src="http://l.yimg.com/a/i/us/we/52/29.gif"/&gt;
&lt;BR /&gt;
&lt;b&gt;Current Conditions:&lt;/b&gt;
&lt;BR /&gt;Partly Cloudy
&lt;BR /&gt;
&lt;BR /&gt;
&lt;b&gt;Forecast:&lt;/b&gt;
&lt;BR /&gt; Mon - Partly Cloudy. High: 77Low: 66
&lt;BR /&gt; Tue - Scattered Showers. High: 73Low: 61
&lt;BR /&gt; Wed - Cloudy. High: 69Low: 59
&lt;BR /&gt; Thu - Cloudy. High: 67Low: 60
&lt;BR /&gt; Fri - Mostly Cloudy. High: 72Low: 63
&lt;BR /&gt;
&lt;BR /&gt;
&lt;a href="http://us.rd.yahoo.com/dailynews/rss/weather/Country__Country/*https://weather.yahoo.com/country/state/city-2161842/"&gt;Full Forecast at Yahoo! Weather&lt;/a&gt;
&lt;BR /&gt;
&lt;BR /&gt;
(provided by &lt;a href="http://www.weather.com" &gt;The Weather Channel&lt;/a&gt;)
&lt;BR /&gt;
]]&gt;</description>
                <guid isPermaLink="false"/>
            </item>
        </channel>
    </results>
</query>

'''
weather = parse_weather(data)

print('Weather:', str(weather))


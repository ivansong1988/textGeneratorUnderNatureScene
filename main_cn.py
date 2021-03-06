# -*- coding: cp936 -*-
import os
import sys
import os.path
import random
import math
import Image
import string
import python2access_cn

global colors
colors = ['snow', 'snow1', 'snow2', 'RosyBrown1', 'RosyBrown2', 'snow3', 'LightCoral', 'IndianRed1', 'RosyBrown3', 'IndianRed2', 'RosyBrown', 'brown1', 'firebrick1', 'brown2', 'IndianRed', 'IndianRed3', 'firebrick2', 'snow4', 'brown3', 'red', 'red1', 'RosyBrown4', 'firebrick3', 'red2', 'firebrick', 'brown', 'red3', 'IndianRed4', 'brown4', 'firebrick4', 'DarkRed', 'red4', 'maroon', 'LightPink1', 'LightPink3', 'LightPink4', 'LightPink2', 'LightPink', 'pink', 'crimson', 'pink1', 'pink2', 'pink3', 'pink4', 'PaleVioletRed4', 'PaleVioletRed', 'PaleVioletRed2', 'PaleVioletRed1', 'PaleVioletRed3', 'LavenderBlush', 'LavenderBlush1', 'LavenderBlush3', 'LavenderBlush2', 'LavenderBlush4', 'maroon', 'HotPink3', 'VioletRed3', 'VioletRed1', 'VioletRed2', 'VioletRed4', 'HotPink2', 'HotPink1', 'HotPink4', 'HotPink', 'DeepPink', 'DeepPink1', 'DeepPink2', 'DeepPink3', 'DeepPink4', 'maroon1', 'maroon2', 'maroon3', 'maroon4', 'MediumVioletRed', 'VioletRed', 'orchid2', 'orchid', 'orchid1', 'orchid3', 'orchid4', 'thistle1', 'thistle2', 'plum1', 'plum2', 'thistle', 'thistle3', 'plum', 'violet', 'plum3', 'thistle4', 'fuchsia', 'magenta', 'magenta1', 'plum4', 'magenta2', 'magenta3', 'DarkMagenta', 'magenta4', 'purple', 'MediumOrchid', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3', 'MediumOrchid4', 'DarkViolet', 'DarkOrchid', 'DarkOrchid1', 'DarkOrchid3', 'DarkOrchid2', 'DarkOrchid4', 'purple', 'indigo', 'BlueViolet', 'purple2', 'purple3', 'purple4', 'purple1', 'MediumPurple', 'MediumPurple1', 'MediumPurple2', 'MediumPurple3', 'MediumPurple4', 'DarkSlateBlue', 'LightSlateBlue', 'MediumSlateBlue', 'SlateBlue', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3', 'SlateBlue4', 'GhostWhite', 'lavender', 'blue', 'blue1', 'blue2', 'blue3', 'MediumBlue', 'blue4', 'DarkBlue', 'MidnightBlue', 'navy', 'NavyBlue', 'RoyalBlue', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'CornflowerBlue', 'LightSteelBlue', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3', 'LightSteelBlue4', 'SlateGray4', 'SlateGray1', 'SlateGray2', 'SlateGray3', 'LightSlateGray', 'LightSlateGrey', 'SlateGray', 'SlateGrey', 'DodgerBlue', 'DodgerBlue1', 'DodgerBlue2', 'DodgerBlue4', 'DodgerBlue3', 'AliceBlue', 'SteelBlue4', 'SteelBlue', 'SteelBlue1', 'SteelBlue2', 'SteelBlue3', 'SkyBlue4', 'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'LightSkyBlue', 'LightSkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2', 'LightSkyBlue3', 'SkyBlue', 'LightBlue3', 'DeepSkyBlue', 'DeepSkyBlue1', 'DeepSkyBlue2', 'DeepSkyBlue4', 'DeepSkyBlue3', 'LightBlue1', 'LightBlue2', 'LightBlue', 'LightBlue4', 'PowderBlue', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3', 'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cadet blue', 'CadetBlue', 'DarkTurquoise', 'azure', 'azure1', 'LightCyan', 'LightCyan1', 'azure2', 'LightCyan2', 'PaleTurquoise1', 'PaleTurquoise', 'PaleTurquoise2', 'DarkSlateGray1', 'azure3', 'LightCyan3', 'DarkSlateGray2', 'PaleTurquoise3', 'DarkSlateGray3', 'azure4', 'LightCyan4', 'aqua', 'cyan', 'cyan1', 'PaleTurquoise4', 'cyan2', 'DarkSlateGray4', 'cyan3', 'cyan4', 'DarkCyan', 'teal', 'DarkSlateGray', 'DarkSlateGrey', 'MediumTurquoise', 'LightSeaGreen', 'turquoise', 'aquamarine4', 'aquamarine', 'aquamarine1', 'aquamarine2', 'aquamarine3', 'MediumAquamarine', 'MediumSpringGreen', 'MintCream', 'SpringGreen', 'SpringGreen1', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4', 'MediumSeaGreen', 'SeaGreen', 'SeaGreen3', 'SeaGreen1', 'SeaGreen4', 'SeaGreen2', 'MediumForestGreen', 'honeydew', 'honeydew1', 'honeydew2', 'DarkSeaGreen1', 'DarkSeaGreen2', 'PaleGreen1', 'PaleGreen', 'honeydew3', 'LightGreen', 'PaleGreen2', 'DarkSeaGreen3', 'DarkSeaGreen', 'PaleGreen3', 'honeydew4', 'green1', 'lime', 'LimeGreen', 'DarkSeaGreen4', 'green2', 'PaleGreen4', 'green3', 'ForestGreen', 'green4', 'green', 'DarkGreen', 'LawnGreen', 'chartreuse', 'chartreuse1', 'chartreuse2', 'chartreuse3', 'chartreuse4', 'GreenYellow', 'DarkOliveGreen3', 'DarkOliveGreen1', 'DarkOliveGreen2', 'DarkOliveGreen4', 'DarkOliveGreen', 'OliveDrab', 'OliveDrab1', 'OliveDrab2', 'OliveDrab3', 'YellowGreen', 'OliveDrab4', 'ivory', 'ivory1', 'LightYellow', 'LightYellow1', 'beige', 'ivory2', 'LightGoldenrodYellow', 'LightYellow2', 'ivory3', 'LightYellow3', 'ivory4', 'LightYellow4', 'yellow', 'yellow1', 'yellow2', 'yellow3', 'yellow4', 'olive', 'DarkKhaki', 'khaki2', 'LemonChiffon4', 'khaki1', 'khaki3', 'khaki4', 'PaleGoldenrod', 'LemonChiffon', 'LemonChiffon1', 'khaki', 'LemonChiffon3', 'LemonChiffon2', 'MediumGoldenRod', 'cornsilk4', 'gold', 'gold1', 'gold2', 'gold3', 'gold4', 'LightGoldenrod', 'LightGoldenrod4', 'LightGoldenrod1', 'LightGoldenrod3', 'LightGoldenrod2', 'cornsilk3', 'cornsilk2', 'cornsilk', 'cornsilk1', 'goldenrod', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4', 'DarkGoldenrod', 'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4', 'FloralWhite', 'wheat2', 'OldLace', 'wheat', 'wheat1', 'wheat3', 'orange', 'orange1', 'orange2', 'orange3', 'orange4', 'wheat4', 'moccasin', 'PapayaWhip', 'NavajoWhite3', 'BlanchedAlmond', 'NavajoWhite', 'NavajoWhite1', 'NavajoWhite2', 'NavajoWhite4', 'AntiqueWhite4', 'AntiqueWhite', 'tan', 'bisque4', 'burlywood', 'AntiqueWhite2', 'burlywood1', 'burlywood3', 'burlywood2', 'AntiqueWhite1', 'burlywood4', 'AntiqueWhite3', 'DarkOrange', 'bisque2', 'bisque', 'bisque1', 'bisque3', 'DarkOrange1', 'linen', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4', 'peru', 'tan1', 'tan2', 'tan3', 'tan4', 'PeachPuff', 'PeachPuff1', 'PeachPuff4', 'PeachPuff2', 'PeachPuff3', 'SandyBrown', 'seashell4', 'seashell2', 'seashell3', 'chocolate', 'chocolate1', 'chocolate2', 'chocolate3', 'chocolate4', 'SaddleBrown', 'seashell', 'seashell1', 'sienna4', 'sienna', 'sienna1', 'sienna2', 'sienna3', 'LightSalmon3', 'LightSalmon', 'LightSalmon1', 'LightSalmon4', 'LightSalmon2', 'coral', 'OrangeRed', 'OrangeRed1', 'OrangeRed2', 'OrangeRed3', 'OrangeRed4', 'DarkSalmon', 'salmon1', 'salmon2', 'salmon3', 'salmon4', 'coral1', 'coral2', 'coral3', 'coral4', 'tomato4', 'tomato', 'tomato1', 'tomato2', 'tomato3', 'MistyRose4', 'MistyRose2', 'MistyRose', 'MistyRose1', 'salmon', 'MistyRose3', 'white', 'gray100', 'grey100', 'grey100', 'gray99', 'grey99', 'gray98', 'grey98', 'gray97', 'grey97', 'gray96', 'grey96', 'WhiteSmoke', 'gray95', 'grey95', 'gray94', 'grey94', 'gray93', 'grey93', 'gray92', 'grey92', 'gray91', 'grey91', 'gray90', 'grey90', 'gray89', 'grey89', 'gray88', 'grey88', 'gray87', 'grey87', 'gainsboro', 'gray86', 'grey86', 'gray85', 'grey85', 'gray84', 'grey84', 'gray83', 'grey83', 'LightGray', 'LightGrey', 'gray82', 'grey82', 'gray81', 'grey81', 'gray80', 'grey80', 'gray79', 'grey79', 'gray78', 'grey78', 'gray77', 'grey77', 'gray76', 'grey76', 'silver', 'gray75', 'grey75', 'gray74', 'grey74', 'gray73', 'grey73', 'gray72', 'grey72', 'gray71', 'grey71', 'gray70', 'grey70', 'gray69', 'grey69', 'gray68', 'grey68', 'gray67', 'grey67', 'DarkGray', 'DarkGrey', 'gray66', 'grey66', 'gray65', 'grey65', 'gray64', 'grey64', 'gray63', 'grey63', 'gray62', 'grey62', 'gray61', 'grey61', 'gray60', 'grey60', 'gray59', 'grey59', 'gray58', 'grey58', 'gray57', 'grey57', 'gray56', 'grey56', 'gray55', 'grey55', 'gray54', 'grey54', 'gray53', 'grey53', 'gray52', 'grey52', 'gray51', 'grey51', 'fractal', 'gray50', 'grey50', 'gray', 'gray49', 'grey49', 'gray48', 'grey48', 'gray47', 'grey47', 'gray46', 'grey46', 'gray45', 'grey45', 'gray44', 'grey44', 'gray43', 'grey43', 'gray42', 'grey42', 'DimGray', 'DimGrey', 'gray41', 'grey41', 'gray40', 'grey40', 'gray39', 'grey39', 'gray38', 'grey38', 'gray37', 'grey37', 'gray36', 'grey36', 'gray35', 'grey35', 'gray34', 'grey34', 'gray33', 'grey33', 'gray32', 'grey32', 'gray31', 'grey31', 'gray30', 'grey30', 'gray29', 'grey29', 'gray28', 'grey28', 'gray27', 'grey27', 'gray26', 'grey26', 'gray25', 'grey25', 'gray24', 'grey24', 'gray23', 'grey23', 'gray22', 'grey22', 'gray21', 'grey21', 'gray20', 'grey20', 'gray19', 'grey19', 'gray18', 'grey18', 'gray17', 'grey17', 'gray16', 'grey16', 'gray15', 'grey15', 'gray14', 'grey14', 'gray13', 'grey13', 'gray12', 'grey12', 'gray11', 'grey11', 'gray10', 'grey10', 'gray9', 'grey9', 'gray8', 'grey8', 'gray7', 'grey7', 'gray6', 'grey6', 'gray5', 'grey5', 'gray4', 'grey4', 'gray3', 'grey3', 'gray2', 'grey2', 'gray1', 'grey1', 'black', 'gray0', 'grey0', 'opaque', 'none', 'transparent']


def pathWalk(path):
    paths = []
    for root, dirs, files in os.walk( path ):
        for fn in files:
            paths.append([root, fn])
    return paths

def generator(words):
    fonts = pathWalk('fonts/font_cn/')
    randomFont = random.choice(fonts)
    randomFont = randomFont[0] + '/' + randomFont[1]

    bgImgs = pathWalk('sceneDataset/')
    randomBgImg = random.choice(bgImgs)
    randomBgImg = randomBgImg[0] + '/' +randomBgImg[1]
    
    #words = raw_input("input words, please:")
    words = words.encode('utf-8')
    saveName = './dataset/' + words + '.png'
    length = len(words)#blank is included
    pointsize = 72
    wordsHeight = pointsize
    wordsWidth = int(pointsize * 5/7) * length
    #whether slant, yes or no both with probility 50%
    if random.randint(1, 2) == 1:
        rotateX = random.randint(1, 10);
    else:
        rotateX = random.randint(350, 360);
    #whether italic, yes or no both with probility 50%
    if random.randint(1, 2) == 1:
        rotateY = rotateX + random.randint(15, 25)
    else:
        rotateY = rotateX
    '''#adjust the size of bg and position of text'''
    #alpha = math.pi * 2 - math.pi / 180 * rotateX
    #wordsHeightRotate = wordsWidth * math.sin(alpha) + wordsHeight * math.cos(alpha)
    #wordsWidthRotate = wordsWidth * math.cos(alpha) + wordsHeight * math.sin(alpha)
    '''calculate some parameter'''
    #sizeHeight = wordsHeight + 20*2;#fix the height
    #sizeWidth = wordsWidthRotate + 20*2;
    #offsetX = random.randint(25, 35) + wordsHeight * math.sin(alpha);
    ##offsetY = random.randint(20, 30) + wordsHeightRotate;
    #offsetY = int((wordsHeightRotate + sizeHeight)/2)
    sizeHeight = wordsHeight + 20*2;
    sizeWidth = wordsWidth + 20*2;
    #offsetX = random.randint(25, 35);
    #offsetY = random.randint(25, 35) + wordsHeight;
    #print rotateX, rotateY, offsetX, offsetY
    sizeWeightHeight = str(sizeWidth) + 'x' + str(sizeHeight)
    #sizeAnnotote = str(rotateX) + 'x' + str(rotateY) + '+' + str(offsetX) + '+' + str(offsetY)
    #shadowAnnotote = str(rotateX) + 'x' + str(rotateY) + '+' + str(offsetX+5) + '+' + str(offsetY+5)
    sizeAnnotote = str(rotateX) + 'x' + str(rotateY)
    shadowAnnotote = str(rotateX) + 'x' + str(rotateY) + '+5+5 '

    print '---------------step1: font rendering---------------'
    #中文字体都不能居中，英文字体都可以
    command = 'convert -size ' + sizeWeightHeight + ' xc:transparent' + ' -font ' + randomFont + ' -pointsize ' + str(pointsize)
    #pure or gradient color, yes or no both with probility 50%
    command = command + ' -gravity center '
    if random.randint(1, 2) == 1:
        randomColor = random.choice(colors)
        command = command + ' -gravity center ' + ' -fill ' + randomColor + ' '
    else:
        randomColor1 = random.choice(colors)
        randomColor2 = random.choice(colors)
        command = command + ' -tile gradient:' + randomColor1 + '-' + randomColor2 + ' '
    print '---------------step1: font rendering finished---------------'

        
    print '---------------step2: border/shadow rendering---------------'
    #whether shadow, yes or no both with probility 50%
    if random.randint(1, 2) == 1:
        command = command + ' -gravity center ' + ' -annotate ' + shadowAnnotote + ' ' + words + ' -blur 0x4 '
        print 'shadow'
    else:
        command = command + ' -gravity center '
        print 'no shadow'
    #single stroke, double stroke or none, yes or no both with probility 50%
    tmp = random.randint(1, 3)
    if tmp == 1:
        command = command + ' -gravity center ' + ' -stroke navy -strokewidth 2 '
        command = command + ' -annotate ' + sizeAnnotote + ' ' + words + ' '
        print '1 stroke'
    elif tmp == 2:
        command = command + ' -gravity center ' + ' -stroke black -strokewidth 3 '
        command = command + ' -annotate ' + sizeAnnotote + ' ' + words + ' '
        command = command + ' -gravity center ' + ' -stroke white -strokewidth 1 '
        command = command + ' -annotate ' + sizeAnnotote + ' ' + words + ' '
        print '2 stroke'
    else:
        command = command + ' -gravity center ' + ' -annotate ' + sizeAnnotote + ' ' + words + ' '
        print 'no stroke'
    print '---------------step2: border/shadow rendering finished---------------'


    print '---------------step3: base color---------------'
    print type(saveName)
    print saveName
    command = command + saveName

    os.system(command)
    print command
    print '---------------step3: base color finished---------------'


    print '---------------step4: projective distortion---------------'
    '''these features haven't been considered'''
    #command = command + ' -wave -50x640 -crop x110+0+10 '
    print '---------------step4: projective distortion finished---------------'


    print '---------------step5: natural data blending---------------'
    command = 'convert -crop '
    command = command + str(sizeWidth) + 'x' + str(sizeHeight) + '+0+0 ' + randomBgImg + ' tmp.png '
    os.system(command)
    #front 30% + bg 70%
    command = 'composite -gravity northwest -blend 90 ' + saveName + ' ' + ' tmp.png ' + ' ' + saveName
    os.system(command)
    randomBlur = random.randint(60, 90)
    command = ' convert -blur ' + str(randomBlur) + ' ' + saveName + ' ' + saveName
    #-blur 80x5
    os.system(command)
    print '---------------step5: natural data blending finished---------------'

    
    print '---------------step6: noise making---------------'
    #whether blur, with probility 25%
    #if random.randint(1, 4) == 1:
    #    command = command + ' -blur 0x3 '
    '''these features haven't been considered'''
    #make the whole font look like it is a 3 dimensional mountain ridge
    #command = command + ' -shade 135x30 -auto-level +level 10,90% '
    #mooth the result to generate a better and strangely shiny look to the resulting font
    #command = command + ' -adaptive-blur 0x2 '
    swirl = random.randint(1, 5)
    command = ' convert -swirl ' + str(swirl) + ' ' + saveName + ' ' + saveName
    os.system(command)
    command = ' convert -noise 5 ' + saveName + ' ' + saveName
    os.system(command)
    #command = 'convert '+ saveName + ' -colorspace Gray '+ saveName
    #os.system(command)
    print '---------------step6: noise making finished---------------'
    
if __name__ == '__main__':
    for i in range(1, 10):
        num = random.randint(5, 10)
        #words = string.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], num)).replace(' ','')
        words = python2access_cn.randomWords_cn()
        generator(words)
        #os.system("pause")

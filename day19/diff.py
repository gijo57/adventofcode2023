from collections import Counter

list1 = [
    ['7', '520', '217', '6'],
    ['1581', '287', '143', '1681'],
    ['655', '487', '13', '2530'],
    ['1751', '1503', '126', '502'],
    ['1244', '168', '348', '136'],
    ['2235', '199', '2207', '237'],
    ['203', '27', '1449', '54'],
    ['1303', '833', '5', '2616'],
    ['1759', '41', '2028', '2797'],
    ['654', '160', '87', '2620'],
    ['201', '15', '1101', '251'],
    ['1270', '1337', '732', '273'],
    ['291', '2915', '3141', '759'],
    ['98', '223', '387', '124'],
    ['806', '1847', '277', '2653'],
    ['1327', '3102', '637', '260'],
    ['14', '549', '1095', '313'],
    ['803', '925', '250', '2091'],
    ['26', '161', '755', '124'],
    ['445', '1320', '359', '367'],
    ['212', '719', '3037', '1565'],
    ['667', '1771', '455', '2370'],
    ['2338', '505', '2285', '197'],
    ['282', '325', '1145', '596'],
    ['3203', '2041', '3037', '861'],
    ['785', '818', '51', '2313'],
    ['355', '517', '32', '2320'],
    ['880', '474', '744', '163'],
    ['1887', '452', '156', '43'],
    ['314', '1417', '1425', '949'],
    ['580', '316', '543', '20'],
    ['1544', '307', '148', '598'],
    ['1338', '474', '1', '85'],
    ['1119', '141', '2187', '927'],
    ['2090', '395', '1095', '48'],
    ['1924', '1593', '86', '489'],
    ['187', '815', '1244', '664'],
    ['472', '180', '923', '443'],
    ['68', '2255', '2883', '1576'],
    ['1341', '15', '2238', '265'],
    ['1582', '832', '793', '1821'],
    ['730', '417', '88', '2828'],
    ['735', '2338', '358', '387'],
    ['45', '2976', '351', '337'],
    ['1019', '586', '756', '475'],
    ['409', '241', '25', '596'],
    ['566', '3236', '643', '301'],
    ['1214', '17', '3358', '880'],
    ['164', '409', '274', '70'],
    ['165', '2122', '642', '1213'],
    ['2546', '749', '3016', '2875'],
    ['222', '2772', '1671', '33'],
    ['464', '494', '1402', '172'],
    ['98', '366', '782', '3305'],
    ['1057', '1816', '2', '2437'],
    ['20', '1901', '3882', '471'],
    ['1564', '633', '485', '171'],
    ['3053', '26', '1201', '36'],
    ['537', '1415', '2285', '742'],
    ['157', '1003', '44', '2287'],
    ['2280', '800', '3070', '633'],
    ['3195', '2527', '809', '2109'],
    ['443', '386', '669', '217'],
    ['352', '3446', '1156', '298'],
    ['234', '459', '1347', '78'],
    ['60', '94', '1007', '264'],
    ['388', '1596', '3322', '321'],
    ['1361', '398', '123', '483'],
    ['529', '2401', '3341', '617'],
    ['1357', '2699', '1840', '108'],
    ['1501', '42', '1765', '7'],
    ['455', '208', '399', '134'],
    ['620', '3048', '766', '436'],
    ['287', '168', '155', '359'],
    ['877', '268', '398', '2263'],
    ['274', '565', '1250', '243'],
    ['557', '2514', '452', '398'],
    ['924', '204', '657', '361'],
    ['541', '2025', '1571', '2620'],
    ['91', '257', '1162', '243'],
    ['222', '477', '1089', '78'],
    ['2048', '1692', '3643', '771'],
    ['301', '2792', '22', '567'],
    ['293', '1152', '2229', '1121'],
    ['977', '3522', '284', '11'],
    ['759', '1225', '579', '2665'],
    ['1038', '1944', '986', '130'],
    ['621', '1251', '1130', '264'],
    ['597', '1687', '1704', '313'],
    ['857', '459', '3229', '602'],
    ['27', '576', '1162', '27'],
    ['147', '1606', '1739', '892'],
    ['913', '242', '1129', '241'],
    ['1943', '368', '3271', '465'],
    ['27', '94', '1237', '360'],
    ['756', '1656', '575', '569'],
    ['1271', '1637', '785', '2471']
]
list2 = [
    ['932', '2862', '1975', '1197'],
    ['1581', '287', '143', '1681'],
    ['655', '487', '13', '2530'],
    ['1751', '1503', '126', '502'],
    ['1948', '602', '227', '394'],
    ['2235', '199', '2207', '237'],
    ['1303', '833', '5', '2616'],
    ['407', '1128', '585', '1854'],
    ['1759', '41', '2028', '2797'],
    ['654', '160', '87', '2620'],
    ['2255', '1072', '487', '1307'],
    ['2374', '392', '197', '1186'],
    ['1270', '1337', '732', '273'],
    ['291', '2915', '3141', '759'],
    ['806', '1847', '277', '2653'],
    ['152', '31', '2019', '214'],
    ['1327', '3102', '637', '260'],
    ['803', '925', '250', '2091'],
    ['445', '1320', '359', '367'],
    ['212', '719', '3037', '1565'],
    ['1612', '41', '119', '1171'],
    ['394', '87', '2515', '137'],
    ['3170', '1480', '1660', '2427'],
    ['667', '1771', '455', '2370'],
    ['2338', '505', '2285', '197'],
    ['355', '517', '32', '2320'],
    ['314', '1417', '1425', '949'],
    ['1270', '1227', '239', '147'],
    ['1119', '141', '2187', '927'],
    ['173', '119', '254', '1160'],
    ['472', '180', '923', '443'],
    ['961', '1136', '400', '418'],
    ['68', '2255', '2883', '1576'],
    ['331', '185', '1787', '1397'],
    ['1341', '15', '2238', '265'],
    ['88', '2065', '1867', '1499'],
    ['481', '2118', '522', '985'],
    ['128', '31', '1115', '1139'],
    ['1582', '832', '793', '1821'],
    ['730', '417', '88', '2828'],
    ['1017', '525', '402', '1384'],
    ['1168', '233', '423', '1256'],
    ['1019', '586', '756', '475'],
    ['1502', '142', '138', '2148'],
    ['687', '2860', '1046', '1692'],
    ['2432', '2368', '458', '677'],
    ['3265', '797', '560', '2373'],
    ['1214', '17', '3358', '880'],
    ['165', '2122', '642', '1213'],
    ['222', '2772', '1671', '33'],
    ['537', '1051', '1831', '3086'],
    ['85', '1936', '1371', '1794'],
    ['1304', '724', '1899', '294'],
    ['1057', '1816', '2', '2437'],
    ['517', '46', '2038', '28'],
    ['20', '1901', '3882', '471'],
    ['340', '1305', '1753', '146'],
    ['1564', '633', '485', '171'],
    ['537', '1415', '2285', '742'],
    ['157', '1003', '44', '2287'],
    ['2280', '800', '3070', '633'],
    ['1114', '1412', '458', '1815'],
    ['897', '835', '2047', '176'],
    ['72', '331', '459', '2983'],
    ['388', '1596', '3322', '321'],
    ['1361', '398', '123', '483'],
    ['1755', '265', '2042', '101'],
    ['3135', '1342', '1262', '2395'],
    ['1262', '962', '1971', '3012'],
    ['529', '2401', '3341', '617'],
    ['1357', '2699', '1840', '108'],
    ['24', '260', '1871', '2953'],
    ['1', '511', '2647', '194'],
    ['3523', '319', '3284', '1244'],
    ['18', '1408', '57', '141'],
    ['29', '330', '5', '1147'],
    ['2048', '1692', '3643', '771'],
    ['301', '2792', '22', '567'],
    ['741', '310', '727', '1519'],
    ['293', '1152', '2229', '1121'],
    ['6', '1161', '60', '629'],
    ['977', '3522', '284', '11'],
    ['759', '1225', '579', '2665'],
    ['351', '1116', '605', '323'],
    ['636', '2243', '2326', '215'],
    ['857', '459', '3229', '602'],
    ['147', '1606', '1739', '892'],
    ['1943', '368', '3271', '465'],
    ['703', '1000', '523', '2228'],
    ['1271', '1637', '785', '2471']
]

c1 = Counter([str(x) for x in list1])
c2 = Counter([str(x) for x in list2])

print(c2 - c1)

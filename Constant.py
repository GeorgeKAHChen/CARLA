############################################################
#
#		CARLA
#		Copyright(c) KazukiAmakawa, all right reserved.
#		Constant.py
#
############################################################
#Here are constants of all the program

MODEL = "TEST"
#This parameter is using for model of all algorithm
#"VPS" means this program will work on vps and not print anything.
#"PRE" means this program will use in presentation and will print all data
#"TEST" means this program is in test model

DataArr = [[169.2, 63.5], [159.2, 53.1], [168.2, 61.4], [158.8, 52.4], [163.8, 56.5], [161.8, 54.4], [157, 52.8], [166.3, 61.4], [154.2, 48.7], [160.6, 53.8], [169.8, 64], [161.1, 53.1], [163.1, 58.2], [178.8, 69.4], [156.9, 52.7], [161.5, 54.2], [160, 47.9], [165.5, 56], [153.5, 45.5], [158.5, 45.3], [161.6, 55.1], [161.8, 56.1], [158.8, 51.7], [161.8, 54.2], [152.5, 48], [147.8, 43.1], [161.2, 52.8], [159.2, 51.9], [162.4, 50.3], [155.2, 49.4], [158, 51.5], [160.7, 52.6], [160.1, 54.5], [157.5, 52.6], [164.1, 58.7], [158.1, 53], [162.9, 54.1], [155.4, 49.4], [160.4, 52.5], [158.3, 53.5], [165.4, 58.3], [166.8, 64.6], [161.9, 52.9], [166.1, 58], [157.4, 49.9], [159.1, 54.8], [161.7, 53.1], [160.7, 52.5], [173, 63.4], [161.1, 54.7], [157.1, 47.8], [160, 57.6], [156.2, 46.7], [161.4, 56], [161.5, 54.3], [159.6, 49.6], [158.1, 56.1], [160.2, 51.8], [157.9, 56.2], [158.4, 52.6], [153.1, 43.8], [158.1, 43.4], [165.2, 61.4], [157.7, 48.3], [157.2, 47.8], [159.8, 50.7], [159.2, 53.4], [160, 50.4], [158, 50.4], [158.2, 54.7], [160, 52.1], [162.6, 56.7], [164.6, 54.5], [158.5, 49.4], [160, 56.1], [161.5, 50.1], [166.3, 59.3], [158.7, 54.5], [152.9, 46.9], [162.1, 49.7], [160.1, 51.9], [168, 56.7], [167.3, 58], [156.7, 50.5], [169.9, 57.1], [169.9, 64.2], [162.6, 56.2], [163.7, 57.4], [149.2, 44.8], [160.2, 54], [160, 49], [163.2, 55.1], [157.7, 50.2], [167.8, 58.3], [159.6, 53.8], [161.4, 54.8], [166.6, 58], [153.9, 43.6], [166.8, 59.5], [165.6, 59.5], [159.2, 54.2], [168.4, 62.9], [156.6, 49.4], [159.3, 48.7], [162.2, 55.1], [162.7, 54.4], [159.1, 52.3], [160, 52.7], [163.9, 62.4], [157.5, 50.9], [157.8, 49.6], [162.8, 52.7], [155, 49.9], [159.7, 52], [159.8, 53.8], [160.3, 51.1], [165.3, 56.8], [169.4, 60.9], [149.6, 45.4], [153.5, 46.4], [168.6, 60.5], [165.9, 54.9], [162.7, 58], [161, 56.8], [151.6, 46.8], [165.9, 56.9], [153.2, 50], [159.3, 55.1], [162.6, 58.9], [161.1, 51.2], [162.5, 55.7], [165.4, 56], [158.5, 50.2], [156.7, 47.7], [167.2, 56.8], [151.9, 47.6], [159, 57.9], [154.8, 47.5], [159.4, 53.2], [153.8, 48.9], [157.7, 47.5], [159.2, 52.6], [162.2, 55.6], [158.2, 51.5], [156.7, 48], [161.2, 54.6], [153.5, 53.8], [156.9, 56.1], [159, 53], [160.7, 56.2], [165.2, 54.9], [166.9, 60.8], [155.6, 50], [160.9, 49.6], [158.9, 50.9], [160.9, 55], [161.9, 50.8], [163.2, 54.8], [165.9, 57.2], [160.1, 46.5], [155.9, 52.8], [157.1, 52], [164.9, 58.9], [158.6, 51.1], [161.8, 58.3], [161, 50.9], [169.5, 56.5], [165.4, 57.7], [168.6, 61.9], [174.7, 69.5], [162.7, 57.5], [158.9, 55.3], [160.6, 54.5], [155.6, 50], [164.6, 53.5], [159, 52.1], [171.5, 60.2], [165.9, 57.5], [162.9, 57.5], [159.1, 53.7], [155, 48.5], [164.6, 55.5], [163.6, 60.5], [158, 51.8], [154.8, 50.3], [162.7, 53.8], [162.4, 55.7], [160.2, 50], [166.2, 57.2], [161.1, 59.4], [162, 54.2], [166.4, 57.6], [162.3, 54.9], [159.8, 51.4], [157.5, 49.4], [156.6, 51], [165.5, 59.8], [175, 66.4], [160.3, 54.7], [161.4, 51.9], [157.4, 51.5], [156.4, 46.4], [162.7, 55.4], [159.5, 50], [161.9, 51.2], [155.4, 55.4], [162.8, 62.5], [160.1, 53.2], [157.6, 49.5], [167.8, 57.5], [152.1, 45.4], [145, 40.9], [165.9, 58.6], [166.6, 61.1], [163.9, 56.3], [162.9, 62.1], [160.9, 59.3], [160.4, 51.6], [167.5, 60.9], [168.1, 59.4], [162.7, 54.6], [156.6, 52.8], [152.8, 48.5], [160.1, 51.5], [160.8, 48.9], [159.8, 50.5], [165.5, 57.3], [150.7, 45], [159.4, 51.2], [157.5, 54.6], [153.7, 43.9], [159.6, 53.8], [156.2, 49.8], [153.1, 45.6], [161.4, 59.8], [160.3, 52.6], [161.5, 53.9], [159, 50.9], [161.1, 51.1], [162.9, 54.8], [157.7, 47.7], [152.6, 42.5], [157.3, 54.9], [162.1, 57.4], [158.4, 55.7], [160.8, 54.2], [162.1, 55.5], [157.2, 51.4], [158.6, 55.1], [158.5, 53.2], [169.1, 59.2], [154.1, 44.8], [166.7, 58], [172.9, 63.5], [159.3, 51], [157.9, 50.6], [159.8, 59.8], [155.8, 47.9], [160.6, 56], [152.7, 47.2], [159.7, 53.8], [157.2, 51.1], [160, 56.7], [158.7, 49.7], [160.4, 54.2], [165.7, 61.7], [160.1, 57.6], [164.6, 58.8], [158.4, 50], [168.8, 62.3], [156.6, 49.8], [160.3, 53.5], [157.8, 49.9], [158.5, 52.3], [161.7, 52.7], [158.1, 51.9], [165.4, 59.1], [156.8, 49], [160.9, 50.5], [161.7, 56], [160, 52.5], [162, 54.6], [160.9, 55], [164.2, 53.1], [158.1, 54.8], [165, 57.4], [166.7, 60.7], [163.7, 51.3], [157.7, 51.7], [152.4, 49.6], [158.4, 52.5], [162.1, 56.7], [156.5, 49.1], [167.2, 65.8], [164, 58.1], [157.2, 48.5], [165.5, 59.6], [160.7, 50.7], [159, 50.8], [158.6, 50.1], [158.6, 50.5], [161.7, 57.5], [161, 53.2], [154.8, 48.4], [156.4, 54.4], [156.9, 49.9], [165.9, 61.1], [160.7, 55.3], [161.4, 52], [162.1, 59.3], [156.6, 49.5], [159.3, 55.6], [159.2, 49.9], [165.8, 57.9], [158.3, 52.9], [157.1, 51.9], [160.7, 54.1], [160.1, 52.7], [154.1, 48.7], [165.6, 61.1], [163.2, 58.4], [159.3, 53.3], [156.8, 48.8], [161.1, 59.4], [163.2, 57.7], [160, 50.8], [163.3, 54.3], [154.3, 47.9], [158.1, 53.7], [156.1, 48.7], [160, 53.5], [155.5, 43.6], [158.6, 50.3], [164.2, 56.7], [157.9, 45.9], [163.2, 57.3], [157.9, 50.1], [157.2, 50.8], [167.9, 60.9], [172.4, 66.1], [162.9, 51.4], [160.2, 52.5], [166.4, 61.1], [162.6, 54.9], [158.1, 51.7], [164.4, 58.1], [165.9, 59.7], [152.5, 44.6], [159.3, 51.9], [163.6, 55.4], [166.5, 57.1], [159.7, 53.6], [161, 56.7], [159.9, 54.6], [159.4, 50.5], [158.1, 46.1], [159, 55.9], [168.8, 61.4], [155, 49.2], [157.9, 51.5], [157, 46.3], [163.5, 53.6], [160.6, 54.9], [160, 52.2], [153.4, 46.2], [159.4, 54.4], [158.1, 53.4], [163.6, 56.4], [162.9, 55.3], [166, 54.5], [162.3, 53.7], [163.7, 57.2], [163.6, 55.2], [158.2, 48.6], [161.4, 53.7], [158.2, 52.7], [157.2, 52.2], [156.9, 50.4], [158.2, 47.6], [156.1, 46.4], [162, 51.3], [157, 49.2], [163.1, 51.2], [158.7, 50.1], [156.4, 49.7], [163.4, 55.9], [163.7, 55.4], [154.2, 44.8], [166.2, 55], [160.4, 48.9], [158.6, 52.7], [161.5, 55.5], [166, 56.7], [169.4, 60.3], [162.3, 56.8], [164.8, 60.2], [162.3, 53.6], [172.8, 64.7], [158.3, 53.8], [163.2, 53.8], [159.5, 54.2], [167.8, 58.8], [164.4, 54], [168.6, 60.7], [165.4, 61], [155.5, 47.6], [155.4, 53.6], [165, 59.5], [153.9, 47.6], [162.3, 54.1], [162.6, 54.7], [161.1, 58.1], [160.2, 52.7], [155.8, 48.7], [154.6, 43.2], [162.6, 57.2], [158.6, 49.8], [165.1, 58.1], [160.4, 54.8], [162.2, 51.2], [153.8, 48.5], [157.8, 51.2], [160.1, 55.1], [168, 58.5], [168.2, 59.1], [161.6, 56.6], [157.7, 53.6], [181.2, 67.5], [166, 57.4], [162.3, 58.1], [169.7, 61.2], [160, 51.3], [165.9, 57.3], [160.1, 54.5], [155.3, 46.9], [165.9, 62.6], [164.4, 58.7], [158.4, 50.4], [161.4, 59.1], [191, 79.4], [161.2, 53.4], [159.7, 52.1], [157, 55.4], [162.9, 57], [161.1, 52], [162.9, 56.8], [154.5, 50], [157.8, 52.5], [160.8, 52.9], [159.9, 56.1], [169.4, 57.1], [157.7, 52], [154.7, 51.5], [150.6, 47.1], [157.5, 51.5], [158.1, 52.8], [169.9, 60.9], [167.7, 61.5], [159.5, 54.1], [159.1, 48.3], [159.1, 52.3], [154.6, 52.8], [164.5, 61.6], [161.4, 55.9], [158.3, 51.7], [155.7, 45.4], [161.3, 55.8], [161.5, 51.3], [160.9, 48.2], [160.8, 52.4], [165.2, 61.5], [160, 50.2], [158.2, 47.3], [156.8, 52.6], [155.9, 51.4], [174.6, 68], [166.2, 55.2], [162.8, 52.2], [157.5, 49.7], [157, 54.6], [167.9, 57.6], [168.3, 60.1], [164.9, 57.5], [162.4, 53.8], [161.5, 51.7], [165.2, 60.1], [159.4, 53.9], [162.4, 57.5], [156.9, 48.5], [157.1, 51.1], [172, 63.2], [161.9, 58.6], [168.4, 56], [161.1, 50.9], [160.8, 54.8], [159.7, 49.8], [158.9, 51.1], [158.2, 52.5], [160.3, 54.6], [164.2, 54.1], [160.7, 52.3], [158.7, 56], [156.9, 50.7], [153.9, 44.7], [153.6, 49.5], [160.2, 52.9], [157.8, 49.1], [153.2, 47.4], [159.5, 54.4], [175.9, 68.2], [163.5, 57.5], [169, 60.3], [161.4, 50.8], [151.9, 43.8], [164.6, 52.7], [160.4, 50.7], [160.3, 54.1], [160.1, 58.8], [157.2, 46.8], [166.2, 58.5], [157.6, 50.9], [167.9, 60.2], [159.9, 58.7], [158.7, 48.1], [161.1, 55.8], [162.4, 56.3], [160.1, 53.3], [154.5, 50.6], [163.1, 64], [163.2, 52.1], [167.2, 59], [162.6, 57.7], [164.8, 53.2], [161.8, 57.7], [162.2, 55.3], [166.9, 55.1], [168.9, 61.8], [150.9, 46.9], [159.5, 48.9], [162, 53.1], [162.9, 55.4], [161, 53], [154.9, 44.6], [156.7, 53.2], [163, 56.1], [159.9, 53.4], [157.1, 51.5], [160.4, 53.6], [158.6, 48.5], [159.6, 52.1], [169.1, 59.7], [155.3, 49.7], [163.8, 55.9], [162.5, 54.2], [156.4, 53.6], [162.6, 57.4], [152.6, 47.1], [158.6, 56.1], [159.4, 51.8], [158.9, 50.6], [160.9, 54.1], [158.2, 51.9], [157.1, 50.5], [161.9, 57.5], [160.7, 48.6], [165.5, 52.5], [162.5, 53.8], [159.3, 50.8], [164.7, 58.5], [158.4, 51.6], [160, 56.8], [161.2, 56.7], [160.4, 50.6], [159.1, 50.8], [163.2, 54.2], [157.3, 53.2], [162.1, 54.2], [159.8, 58], [155.5, 50.3], [160.1, 53.5], [160, 52.8], [160.8, 49.3], [161.6, 50.3], [159.6, 57.9], [162.5, 54.6], [159.8, 52.5], [166.6, 58.4], [161.6, 52.6], [158.2, 52.2], [159.8, 53.4], [158.6, 52.5], [160.5, 52.9], [157.5, 50.7], [160.4, 52], [156.7, 48.6], [154, 47.7], [153.7, 46.3], [159.1, 51.3], [160.8, 54.6], [161.7, 56.5], [163.5, 55.6], [164, 57.1], [164.2, 59], [166.6, 61.5], [159.4, 54.8], [155.3, 49.1], [157.2, 45.2], [162, 55.7], [159.2, 55.2], [159.8, 53.5], [158.8, 50.1], [161.8, 57.1], [160.3, 57.6], [158.9, 51.9], [157.4, 50.1], [147, 44.4], [158.6, 51.3], [160.7, 55.8], [156.6, 50.6], [160, 49.9], [159, 52], [160.7, 53.4], [168.1, 58.2], [161.3, 51.3], [161, 53.7], [162.3, 57], [159.3, 48.1], [166.1, 57.7], [162.4, 58.9], [161.4, 54.9], [163.7, 56.9], [158.9, 50.7], [156.9, 50.3], [161.4, 52.1], [165.8, 55.7], [165.4, 60.5], [162.6, 54.4], [157.2, 51.2], [158, 51.3], [166.5, 56.7], [184.6, 72.3], [164.4, 53.4], [161, 58], [159.6, 55.2], [164.7, 55.6], [168.1, 61.8], [162, 48.9], [169.2, 62.9], [162.6, 55.1], [160.4, 54.1], [154.4, 44.7], [165.1, 57.4], [158.5, 49.4], [173.3, 63.1], [159.2, 53.6], [160.5, 55], [164.4, 58.3], [158, 47.6], [162.8, 57.3], [163.7, 52.8], [165.3, 59.3], [162.1, 52.7], [163.4, 56], [159.3, 52.2], [161, 51.5], [157.9, 53.8], [165, 57.5], [157.8, 49.7], [161.7, 54.2], [158.3, 51.6], [153.6, 49.7], [162.6, 56.4], [161.4, 54.4], [166.9, 57.1], [155.4, 48.1], [157.9, 52.5], [155.9, 51.4], [153.3, 51], [161.1, 61], [154.3, 48.3], [160.8, 52], [155.9, 48.7], [159, 52.3], [164.9, 60.1], [151.3, 47.9], [158.2, 53.1], [160.5, 57.5], [160.8, 51.7], [168, 60.6], [167.7, 61.5], [157.2, 47.5], [164.7, 62.1], [155.9, 47.6], [158.1, 52], [162.8, 54], [157.5, 54.4], [160.1, 48], [159.8, 54.5], [159.4, 47.4], [161.8, 55.7], [164.5, 55.9], [158.2, 51], [155.3, 48.3], [158.9, 52], [157.8, 49.8], [162.9, 56], [156.7, 53.1], [163.4, 57.8], [166.8, 62.7], [157.2, 50.1], [158.8, 54], [158.5, 55.7], [162.7, 59.4], [160.2, 54.5], [157.5, 48.9], [161.2, 53.7], [163, 56.3], [156.1, 51.3], [167.8, 58.7], [159.9, 54.4], [158.6, 52.3], [157.2, 47.9], [158.3, 48.4], [159.8, 57.4], [166.5, 56.4], [158.8, 51.4], [162.2, 59.1], [159.7, 52.4], [160.6, 55], [167.2, 56.7], [158.7, 60.8], [152.3, 45.3], [160.9, 53.6], [157.7, 52.9], [161.7, 51.1], [164.8, 53.2], [161.9, 51.2], [159.1, 53.7], [157.1, 49.5], [158.9, 53.6], [161.8, 54.2], [161.9, 54.5], [153, 43.8], [158.8, 49], [159.4, 56.4], [169.7, 61.6], [157.5, 54.5], [166.4, 56.8], [158.4, 51.6], [153.7, 48.6], [165.8, 57.9], [162.5, 55.7], [162, 57], [160.5, 53.2], [167.5, 59.1], [160, 56.6], [160.6, 55.6], [166.1, 61], [157.6, 52.4], [156.2, 47], [157.4, 51.6], [157.2, 48.1], [141.1, 37.5], [169.5, 56.9], [165.2, 56.4], [157.6, 55.1], [151.1, 47.6], [169.2, 56.1], [163.6, 58.5], [161.8, 54], [160.7, 53.5], [159.3, 53.5], [159.8, 49.4], [158.8, 51], [161.7, 53.9], [167.3, 59], [154, 44.9], [159.9, 54.6], [159, 51.4], [160.5, 51.6], [161, 56.5], [165.8, 58.1], [166.5, 60.9], [160.1, 52.1], [157.3, 54.1], [162.4, 54.3], [157.6, 52.5], [166.4, 57.6], [162.8, 57.8], [154, 47.8], [158.2, 51.1], [162, 54.1], [162.8, 61.5], [163.6, 55.6], [161.8, 54.4], [162.8, 59], [158.7, 59], [157.7, 50.5], [166.7, 57.1], [158.3, 48.3], [160, 47.6], [164.6, 54.4], [162.1, 54.4], [165.2, 60], [172.4, 62.9], [161.4, 51], [157.9, 50.9], [170.2, 60.1], [158.7, 52], [160.2, 52.7], [171.5, 63.8], [169.8, 59.6], [160.8, 57.5], [161.3, 51.2], [161.4, 52.6], [157.9, 55.9], [159.2, 53.4], [157.5, 50], [159, 53.1], [165.7, 56.7], [154.2, 49.7], [166.7, 57.7], [159.9, 50.2], [162.1, 57.4], [160.5, 54.4], [164.3, 57.3], [158.3, 53.4], [152.2, 48.7], [162.2, 56.9], [157.9, 51], [159.6, 57.6], [163.6, 59.9], [174, 61.8], [153.3, 47.3], [171.9, 61.4], [159.4, 50.5], [157.7, 54.9], [158.9, 50.1], [159.9, 52.5], [169.4, 55.6], [155.4, 52], [162.3, 51.9], [160.1, 47.9], [165.9, 56.2], [165.5, 55], [155.2, 50.2], [156.3, 48], [157.4, 55.6], [156.1, 46.2], [155.3, 50.2], [170.6, 61.2], [159, 50.6], [163.7, 57.4], [164.6, 55.4], [158.6, 49.5], [164.2, 59.4], [156.8, 44.9], [150.4, 46.8], [164.6, 54.1], [169.7, 64.5], [162.5, 56.1], [161.9, 56.7], [156.7, 49.9], [162.2, 57.9], [154.6, 47], [156.9, 49.9], [163.1, 55], [158.4, 51.7], [180.1, 68], [163.3, 54.9], [163.9, 58.2], [166, 60.9], [157.1, 49.6], [160.1, 54.6], [162.2, 50], [157.2, 50.6], [160.1, 57.9], [159.8, 51], [174.8, 64.5], [160.8, 52.4], [153.7, 47.2], [167.5, 62.2], [164.5, 57], [159.1, 54.4], [161.2, 52.5], [161.4, 51.5], [159.4, 54.2], [156.2, 51.8], [164, 58], [158.1, 52.5], [170.2, 61], [163.2, 57.2], [165, 58.5], [164.4, 55.4], [156.2, 48.6], [159.9, 56.6], [157.9, 47.8], [158.5, 52.6], [168, 59.7], [162.1, 55.8], [159.8, 52.5], [173.3, 64.6], [166.1, 58.5], [157.8, 51.3], [164.7, 56.8], [157.7, 48.6], [162.6, 56.9], [169.3, 60.2], [153.9, 49], [159.3, 54.4], [161.5, 54.5], [160.3, 54.3], [158.5, 52.4], [160.4, 50.7], [169.6, 63.3], [159.5, 54.1], [157.4, 49.4], [156.5, 48.5], [157.9, 52], [160.2, 52.6], [157.9, 53], [164.9, 58.9], [160.3, 52.6], [159.8, 51], [160.7, 51.3], [164.3, 56.3], [161, 57.6], [167.8, 60.7], [162.5, 58.5], [162, 49.3], [160.8, 49], [162.2, 51], [161.8, 55.8], [160, 54.7], [164.7, 55.4], [163.3, 55.8], [155, 43.8], [160.7, 48.3], [164, 56], [168.1, 59], [162.2, 54.6], [161.8, 58.2], [162.8, 56.4], [162.6, 55], [157.9, 50.4], [158.9, 53.2], [165.2, 57.2], [162.6, 54.2], [157.2, 51.1], [153.8, 50.4], [164.9, 56.5], [165.6, 59.6], [159.4, 50.8], [162.6, 51.4], [162.7, 60.4], [165.2, 55.3], [160.1, 56.7], [164.7, 56.9], [161.8, 58.7], [164, 52.9], [160.2, 53.8], [174.3, 65.5], [157.4, 52.2], [166, 59.6], [156.4, 50.9], [162.5, 50.8], [166.6, 63.5], [155.5, 49.1], [170.4, 61.9], [151.2, 41.8], [166.1, 55], [157.7, 54.9], [161.8, 57.8], [157.4, 48], [169.9, 62], [160.7, 55.3], [160.6, 51.1], [161.9, 55], [155, 47], [154.1, 51.4], [161.6, 54.5], [161.6, 55.3], [157.3, 52], [160.3, 51.9], [161.9, 52.8], [157, 49.3], [155.9, 52.3], [162.7, 56.2], [174, 67.1], [162.4, 57.7], [158.1, 48.4], [155.4, 49.9], [168.3, 62], [162.1, 55.6], [162.6, 57.2], [158.8, 51.6], [168, 53.7], [160.6, 50.6], [158.4, 51.5], [163.6, 50.1]]


#=======================================================
#Parameters and functions followed are the learning object you can change
xmin = 0.0
xmax = 2.0
#Interval min and max
def Consume(x):
	import math
	#This function is used as consume function for every action
	#You can change your parameter if you want to learn other things
	return abs(pow(math.e, x) - 2)

	
#=======================================================
#Parameters and functions followed are the learning parameter you can change
TTLkase = 2000
#Loop total case
gw = 0.02
gh = 0.3
#Parameter about the converge speed in H(x, x_i)
LoopMax = 500
#Parameter which can change the iteration times to uniform distribution in Newton' method

import unittest
import sys
sys.path.insert(0, '/home/team22/repos/supply-backend/src')
from models.Vehicle import Vehicle

class vehicleTests(unittest.TestCase):

    def testVehicleGetters(self):
        testVehicle = Vehicle(5, "Sedan", None, 1, [ -97.7583, 30.2322 ], "A", None)

        # Test getId method
        # Expects ID of 5
        self.assertEqual(testVehicle.getId(), 5)

        # Test getVehicleMakeModel method
        # Expects Vehicle type of 'sedan'
        self.assertEqual(testVehicle.getVehicleMakeModel(), "Sedan")

        # Test getCurrOrderRoutes method
        # Expects null route -> stationary vehicle
        self.assertEqual(testVehicle.getCurrOrderRoutes(), None)

        # Test getStatus method
        # Expects status of 1 -> enum for 'Available'
        self.assertEqual(testVehicle.getStatus(), 1)

        # Test getCurrLocation method
        # Expects current location of [ -92.12323, 54.23123 ] -> lat long of St. Edward's
        self.assertEqual(testVehicle.getCurrLocation(), [ -97.7583, 30.2322 ])

        # Test getFleetName method
        # Expects fleet name "A"
        self.assertEqual(testVehicle.getFleetName(), "A")

        # Test getInventory method
        # Expects inventory of null -> empty vehicle
        self.assertEqual(testVehicle.getInventory(), None)

    def testVehicleSetters(self):
        testVehicle = Vehicle(5, "Sedan", None, 1, [ -97.7583, 30.2322 ], "A", None)

        # Test setId method
        # Expects ID of 5
        self.assertEqual(testVehicle.setId(), 6)

        # Test setVehicleMakeModel method
        # Expects Vehicle type of 'sedan'
        self.assertEqual(testVehicle.setVehicleMakeModel(), "Sedan")

        # Test setCurrOrderRoutes method
        # Expects null route -> stationary vehicle
        self.assertEqual(testVehicle.setCurrOrderRoutes(), [
        [
            -97.753085,
            30.228939
        ],
        [
            -97.752967,
            30.22887
        ],
        [
            -97.753031,
            30.228756
        ],
        [
            -97.753158,
            30.228531
        ],
        [
            -97.753491,
            30.227936
        ],
        [
            -97.753542,
            30.227846
        ],
        [
            -97.753604,
            30.227745
        ],
        [
            -97.753666,
            30.227643
        ],
        [
            -97.753882,
            30.227244
        ],
        [
            -97.754122,
            30.226749
        ],
        [
            -97.753782,
            30.226588
        ],
        [
            -97.75365,
            30.226525
        ],
        [
            -97.753307,
            30.226364
        ],
        [
            -97.753136,
            30.226283
        ],
        [
            -97.752705,
            30.22609
        ],
        [
            -97.752189,
            30.225858
        ],
        [
            -97.751197,
            30.22539
        ],
        [
            -97.750532,
            30.225087
        ],
        [
            -97.750075,
            30.224878
        ],
        [
            -97.749801,
            30.224749
        ],
        [
            -97.748971,
            30.224411
        ],
        [
            -97.748627,
            30.224224
        ],
        [
            -97.748191,
            30.223882
        ],
        [
            -97.747743,
            30.223523
        ],
        [
            -97.747728,
            30.223511
        ],
        [
            -97.74762,
            30.223433
        ],
        [
            -97.747458,
            30.223302
        ],
        [
            -97.747337,
            30.223205
        ],
        [
            -97.747169,
            30.223064
        ],
        [
            -97.747066,
            30.222984
        ],
        [
            -97.746714,
            30.222698
        ],
        [
            -97.746626,
            30.222611
        ],
        [
            -97.746582,
            30.222569
        ],
        [
            -97.74653,
            30.222518
        ],
        [
            -97.746472,
            30.222456
        ],
        [
            -97.74624,
            30.222206
        ],
        [
            -97.745852,
            30.221788
        ],
        [
            -97.745477,
            30.221385
        ],
        [
            -97.745398,
            30.221297
        ],
        [
            -97.745375,
            30.221272
        ],
        [
            -97.745357,
            30.221253
        ],
        [
            -97.745348,
            30.221243
        ],
        [
            -97.745255,
            30.221141
        ],
        [
            -97.744894,
            30.220743
        ],
        [
            -97.744508,
            30.220319
        ],
        [
            -97.744405,
            30.220206
        ],
        [
            -97.744217,
            30.219999
        ],
        [
            -97.744136,
            30.219896
        ],
        [
            -97.744074,
            30.219806
        ],
        [
            -97.744021,
            30.219718
        ],
        [
            -97.74397,
            30.21962
        ],
        [
            -97.743921,
            30.21951
        ],
        [
            -97.74388,
            30.219398
        ],
        [
            -97.743847,
            30.219283
        ],
        [
            -97.743823,
            30.219164
        ],
        [
            -97.743809,
            30.219067
        ],
        [
            -97.743801,
            30.218962
        ],
        [
            -97.7438,
            30.218929
        ],
        [
            -97.7438,
            30.218911
        ],
        [
            -97.7438,
            30.2189
        ],
        [
            -97.7438,
            30.218856
        ],
        [
            -97.743801,
            30.218834
        ],
        [
            -97.743806,
            30.21874
        ],
        [
            -97.743827,
            30.218509
        ],
        [
            -97.743844,
            30.218325
        ],
        [
            -97.743912,
            30.217578
        ],
        [
            -97.743919,
            30.217497
        ],
        [
            -97.74396,
            30.217043
        ],
        [
            -97.743995,
            30.216633
        ],
        [
            -97.743997,
            30.216612
        ],
        [
            -97.744003,
            30.216468
        ],
        [
            -97.744048,
            30.215892
        ],
        [
            -97.744056,
            30.215735
        ],
        [
            -97.743647,
            30.215709
        ],
        [
            -97.742939,
            30.215686
        ],
        [
            -97.741809,
            30.21565
        ],
        [
            -97.741187,
            30.215631
        ],
        [
            -97.74055,
            30.215591
        ],
        [
            -97.740098,
            30.215563
        ],
        [
            -97.738994,
            30.215426
        ],
        [
            -97.738937,
            30.215418
        ],
        [
            -97.737685,
            30.215238
        ],
        [
            -97.736548,
            30.215074
        ],
        [
            -97.736147,
            30.215016
        ],
        [
            -97.735994,
            30.214994
        ],
        [
            -97.73586,
            30.214974
        ],
        [
            -97.735347,
            30.214891
        ],
        [
            -97.734592,
            30.214775
        ],
        [
            -97.734278,
            30.214727
        ],
        [
            -97.733573,
            30.21462
        ],
        [
            -97.733063,
            30.214535
        ],
        [
            -97.731307,
            30.214297
        ],
        [
            -97.730197,
            30.214144
        ],
        [
            -97.729517,
            30.214049
        ],
        [
            -97.729499,
            30.214046
        ],
        [
            -97.72906,
            30.213967
        ],
        [
            -97.728244,
            30.213854
        ],
        [
            -97.727592,
            30.213765
        ],
        [
            -97.727308,
            30.213725
        ],
        [
            -97.726942,
            30.213675
        ],
        [
            -97.726304,
            30.213587
        ],
        [
            -97.725838,
            30.21354
        ],
        [
            -97.724746,
            30.213428
        ],
        [
            -97.723253,
            30.213276
        ],
        [
            -97.721925,
            30.213138
        ],
        [
            -97.721641,
            30.213117
        ],
        [
            -97.72056,
            30.213
        ],
        [
            -97.719435,
            30.212885
        ],
        [
            -97.719142,
            30.212861
        ],
        [
            -97.718567,
            30.21289
        ],
        [
            -97.718395,
            30.212888
        ],
        [
            -97.717756,
            30.212847
        ],
        [
            -97.717075,
            30.212813
        ],
        [
            -97.716794,
            30.212798
        ],
        [
            -97.716318,
            30.212792
        ],
        [
            -97.712891,
            30.212271
        ],
        [
            -97.712057,
            30.212184
        ],
        [
            -97.71174,
            30.212172
        ],
        [
            -97.71132,
            30.212168
        ],
        [
            -97.710756,
            30.212187
        ],
        [
            -97.71002,
            30.212251
        ],
        [
            -97.709603,
            30.212308
        ],
        [
            -97.709106,
            30.212408
        ],
        [
            -97.70822,
            30.212637
        ],
        [
            -97.707531,
            30.212855
        ],
        [
            -97.704096,
            30.213975
        ],
        [
            -97.700942,
            30.21505
        ],
        [
            -97.697811,
            30.216012
        ],
        [
            -97.695246,
            30.21687
        ],
        [
            -97.693067,
            30.217623
        ],
        [
            -97.692687,
            30.217746
        ],
        [
            -97.692241,
            30.217906
        ],
        [
            -97.691067,
            30.218368
        ],
        [
            -97.690883,
            30.218441
        ],
        [
            -97.690878,
            30.218443
        ],
        [
            -97.690868,
            30.218447
        ],
        [
            -97.69068,
            30.218523
        ],
        [
            -97.690646,
            30.218537
        ],
        [
            -97.690491,
            30.218607
        ],
        [
            -97.689731,
            30.218953
        ],
        [
            -97.688216,
            30.219594
        ],
        [
            -97.687224,
            30.220042
        ],
        [
            -97.686321,
            30.220566
        ],
        [
            -97.685331,
            30.221106
        ],
        [
            -97.684802,
            30.221349
        ],
        [
            -97.683925,
            30.221726
        ],
        [
            -97.682813,
            30.222112
        ],
        [
            -97.682418,
            30.222237
        ],
        [
            -97.682025,
            30.222356
        ],
        [
            -97.681793,
            30.222408
        ],
        [
            -97.681605,
            30.222457
        ],
        [
            -97.68124,
            30.222521
        ],
        [
            -97.680824,
            30.222552
        ],
        [
            -97.680219,
            30.222555
        ],
        [
            -97.679121,
            30.222441
        ],
        [
            -97.678024,
            30.22233
        ],
        [
            -97.677289,
            30.222203
        ],
        [
            -97.67641,
            30.221976
        ],
        [
            -97.676056,
            30.221859
        ],
        [
            -97.675727,
            30.221737
        ],
        [
            -97.675529,
            30.221658
        ],
        [
            -97.675357,
            30.221586
        ],
        [
            -97.675011,
            30.221437
        ],
        [
            -97.674788,
            30.22133
        ],
        [
            -97.674433,
            30.221152
        ],
        [
            -97.67415,
            30.221008
        ],
        [
            -97.672208,
            30.220018
        ],
        [
            -97.670907,
            30.219353
        ],
        [
            -97.669875,
            30.218825
        ],
        [
            -97.668765,
            30.218268
        ],
        [
            -97.667713,
            30.217722
        ],
        [
            -97.666716,
            30.217215
        ],
        [
            -97.666353,
            30.217024
        ],
        [
            -97.665948,
            30.216808
        ],
        [
            -97.665627,
            30.21663
        ],
        [
            -97.665297,
            30.21644
        ],
        [
            -97.664039,
            30.215722
        ],
        [
            -97.663548,
            30.215443
        ],
        [
            -97.662373,
            30.214766
        ],
        [
            -97.661132,
            30.214058
        ],
        [
            -97.660697,
            30.213811
        ],
        [
            -97.660253,
            30.21357
        ],
        [
            -97.659847,
            30.213355
        ],
        [
            -97.65905,
            30.212936
        ],
        [
            -97.658415,
            30.212612
        ],
        [
            -97.657995,
            30.212399
        ],
        [
            -97.657632,
            30.212214
        ],
        [
            -97.657439,
            30.212122
        ],
        [
            -97.657155,
            30.211986
        ],
        [
            -97.656518,
            30.211697
        ],
        [
            -97.656091,
            30.211509
        ],
        [
            -97.655885,
            30.211416
        ],
        [
            -97.655626,
            30.211293
        ],
        [
            -97.655437,
            30.211201
        ],
        [
            -97.65509,
            30.211029
        ],
        [
            -97.653989,
            30.21047
        ],
        [
            -97.653663,
            30.210303
        ],
        [
            -97.653221,
            30.21008
        ],
        [
            -97.652616,
            30.209772
        ],
        [
            -97.649816,
            30.208342
        ],
        [
            -97.649207,
            30.208033
        ],
        [
            -97.648187,
            30.207511
        ],
        [
            -97.647578,
            30.207201
        ],
        [
            -97.646385,
            30.206593
        ],
        [
            -97.646158,
            30.206473
        ],
        [
            -97.645963,
            30.206365
        ],
        [
            -97.645876,
            30.206315
        ],
        [
            -97.645844,
            30.206296
        ],
        [
            -97.645708,
            30.206216
        ],
        [
            -97.645537,
            30.206165
        ],
        [
            -97.6455,
            30.206154
        ],
        [
            -97.645331,
            30.206084
        ],
        [
            -97.645189,
            30.206018
        ],
        [
            -97.645116,
            30.205978
        ],
        [
            -97.644892,
            30.205853
        ],
        [
            -97.644784,
            30.205793
        ],
        [
            -97.644538,
            30.205654
        ],
        [
            -97.644195,
            30.205452
        ],
        [
            -97.643389,
            30.20497
        ],
        [
            -97.642776,
            30.204585
        ],
        [
            -97.642259,
            30.204267
        ],
        [
            -97.64173,
            30.203961
        ],
        [
            -97.641381,
            30.203764
        ],
        [
            -97.640953,
            30.203532
        ],
        [
            -97.640609,
            30.203349
        ],
        [
            -97.640118,
            30.203095
        ],
        [
            -97.639111,
            30.202585
        ],
        [
            -97.637367,
            30.201698
        ],
        [
            -97.636647,
            30.201328
        ],
        [
            -97.633496,
            30.199722
        ],
        [
            -97.632629,
            30.199286
        ],
        [
            -97.63251,
            30.199209
        ],
        [
            -97.632377,
            30.199132
        ],
        [
            -97.632075,
            30.198968
        ],
        [
            -97.631799,
            30.198813
        ],
        [
            -97.630655,
            30.198176
        ],
        [
            -97.630407,
            30.198037
        ],
        [
            -97.629659,
            30.197602
        ],
        [
            -97.628607,
            30.196992
        ],
        [
            -97.628153,
            30.196717
        ],
        [
            -97.627915,
            30.196582
        ],
        [
            -97.627765,
            30.196511
        ],
        [
            -97.627645,
            30.196455
        ],
        [
            -97.62743,
            30.196363
        ],
        [
            -97.62723,
            30.196295
        ],
        [
            -97.627053,
            30.196243
        ],
        [
            -97.626849,
            30.19619
        ],
        [
            -97.626637,
            30.196152
        ],
        [
            -97.626391,
            30.196118
        ],
        [
            -97.626113,
            30.196094
        ],
        [
            -97.625886,
            30.19609
        ],
        [
            -97.625645,
            30.196097
        ],
        [
            -97.625389,
            30.196122
        ],
        [
            -97.625141,
            30.196156
        ],
        [
            -97.624884,
            30.196208
        ],
        [
            -97.624627,
            30.196279
        ],
        [
            -97.624375,
            30.196363
        ],
        [
            -97.624175,
            30.196449
        ],
        [
            -97.623887,
            30.196591
        ],
        [
            -97.623653,
            30.196726
        ],
        [
            -97.623463,
            30.196854
        ],
        [
            -97.623219,
            30.19704
        ],
        [
            -97.623059,
            30.197188
        ],
        [
            -97.622846,
            30.197408
        ],
        [
            -97.622621,
            30.197684
        ],
        [
            -97.622462,
            30.197932
        ],
        [
            -97.622342,
            30.198177
        ],
        [
            -97.622234,
            30.198418
        ],
        [
            -97.622154,
            30.198669
        ],
        [
            -97.622098,
            30.198919
        ],
        [
            -97.622065,
            30.199139
        ],
        [
            -97.622044,
            30.199436
        ],
        [
            -97.622049,
            30.199795
        ],
        [
            -97.622057,
            30.200387
        ],
        [
            -97.622078,
            30.202133
        ],
        [
            -97.622093,
            30.203036
        ],
        [
            -97.622177,
            30.204305
        ],
        [
            -97.622174,
            30.20505
        ],
        [
            -97.622209,
            30.208589
        ],
        [
            -97.622292,
            30.213514
        ],
        [
            -97.622273,
            30.220179
        ],
        [
            -97.622282,
            30.222626
        ],
        [
            -97.622247,
            30.223286
        ],
        [
            -97.622127,
            30.22385
        ],
        [
            -97.621947,
            30.224621
        ],
        [
            -97.621664,
            30.225482
        ],
        [
            -97.621423,
            30.226075
        ],
        [
            -97.621131,
            30.226646
        ],
        [
            -97.620811,
            30.227197
        ],
        [
            -97.619947,
            30.228446
        ],
        [
            -97.619445,
            30.229165
        ],
        [
            -97.618702,
            30.23025
        ],
        [
            -97.618432,
            30.230716
        ],
        [
            -97.618162,
            30.231207
        ],
        [
            -97.617012,
            30.233661
        ],
        [
            -97.616625,
            30.234514
        ],
        [
            -97.616007,
            30.235641
        ],
        [
            -97.615638,
            30.236205
        ],
        [
            -97.615284,
            30.236758
        ],
        [
            -97.614891,
            30.237369
        ],
        [
            -97.614432,
            30.238129
        ],
        [
            -97.613647,
            30.239327
        ],
        [
            -97.612128,
            30.241744
        ],
        [
            -97.611304,
            30.242905
        ],
        [
            -97.610496,
            30.243968
        ],
        [
            -97.610023,
            30.244556
        ],
        [
            -97.609466,
            30.245292
        ],
        [
            -97.609241,
            30.245587
        ],
        [
            -97.60891,
            30.246018
        ],
        [
            -97.608877,
            30.246059
        ],
        [
            -97.608843,
            30.246102
        ],
        [
            -97.607992,
            30.247215
        ],
        [
            -97.607493,
            30.247818
        ],
        [
            -97.606947,
            30.248435
        ],
        [
            -97.606502,
            30.248944
        ],
        [
            -97.606136,
            30.249411
        ],
        [
            -97.605985,
            30.249649
        ],
        [
            -97.605743,
            30.25003
        ],
        [
            -97.605122,
            30.251006
        ],
        [
            -97.604821,
            30.251471
        ],
        [
            -97.603689,
            30.25329
        ],
        [
            -97.603614,
            30.253425
        ],
        [
            -97.601723,
            30.252684
        ],
        [
            -97.601536,
            30.252598
        ],
        [
            -97.600566,
            30.252156
        ],
        [
            -97.599781,
            30.251798
        ],
        [
            -97.599286,
            30.251581
        ],
        [
            -97.598974,
            30.251478
        ],
        [
            -97.598783,
            30.251434
        ],
        [
            -97.59861,
            30.251399
        ],
        [
            -97.598471,
            30.251381
        ],
        [
            -97.598346,
            30.251358
        ],
        [
            -97.597546,
            30.251307
        ],
        [
            -97.597168,
            30.251281
        ],
        [
            -97.596864,
            30.25127
        ],
        [
            -97.596335,
            30.251255
        ],
        [
            -97.595789,
            30.251238
        ],
        [
            -97.595668,
            30.251234
        ],
        [
            -97.594765,
            30.251205
        ],
        [
            -97.594002,
            30.251063
        ],
        [
            -97.593786,
            30.251045
        ],
        [
            -97.593484,
            30.251016
        ],
        [
            -97.591549,
            30.250652
        ],
        [
            -97.591227,
            30.250611
        ],
        [
            -97.591042,
            30.250577
        ],
        [
            -97.590465,
            30.250471
        ],
        [
            -97.589866,
            30.250361
        ],
        [
            -97.589538,
            30.2503
        ],
        [
            -97.589219,
            30.250221
        ],
        [
            -97.589069,
            30.250184
        ],
        [
            -97.588757,
            30.250066
        ],
        [
            -97.588581,
            30.249985
        ],
        [
            -97.588433,
            30.249918
        ],
        [
            -97.588059,
            30.249727
        ],
        [
            -97.587801,
            30.249596
        ],
        [
            -97.587519,
            30.249453
        ],
        [
            -97.587628,
            30.249284
        ]
    ])

        # Test setStatus method
        # Expects status of 1 -> enum for 'Available'
        self.assertEqual(testVehicle.setStatus(), 1)

        # Test setCurrLocation method
        # Expects changed current location of [-97.7404, 30.2747] -> lat long Texas Capitol Building
        self.assertEqual(testVehicle.setCurrLocation(), [-97.7404, 30.2747])

        # Test setFleetName method
        # Expects fleet name "A"
        self.assertEqual(testVehicle.setFleetName(), "A")

        # Test setInventory method
        # Expects inventory of null -> empty vehicle
        self.assertEqual(testVehicle.setInventory(), {"covid" : 5})
    #NEED TO TEST NOT NULL ROUTE AND NOT NULL INVENTORY

    def test_str(self):
        testVehicle = Vehicle(5, "Sedan", None, 1, [ -97.7583, 30.2322 ], "A", None)

        self.assertEqual(str(testVehicle), "Vehicle ID: 5\nMake and Model: Sedan\nCurrent Order: None\nStatus: 1\nCurrent Location: [ -97.7583, 30.2322 ] \nFleet Name: A 1\nInventory: None")
        
if __name__ == '__main__':
    unittest.main()
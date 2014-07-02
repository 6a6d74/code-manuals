import os

from ttlhead import ttlhead
import cleanttl
import common

def make_regs():
    if not os.path.exists('ttl/common'):
        common.main()
    if not os.path.exists('ttl/common/c-15'):
        os.mkdir('ttl/common/c-15')
        with open('ttl/common/deprec_c-15.ttl', 'w') as fhandle:
            fhandle.write(ttlhead)
            fhandle.write("""<c-15> a reg:Register , ldp:Container ;
    rdfs:label "Physical quantities"@en ;
    dct:description "WMO No. 306 Vol I.2 Common Code-table C-15 'Physical quantities'."@en ;
    reg:owner <http://codes.wmo.int/system/organization/wmo> ;
    reg:manager <http://codes.wmo.int/system/organization/www-dm> ;
    .
    """)
    if not os.path.exists('ttl/common/c-15/ae'):
        os.mkdir('ttl/common/c-15/ae')
        with open('ttl/common/ae/deprec_ae.ttl', 'w') as fhandle:
            fhandle.write(ttlhead)
            fhandle.write("""<ae>
    a reg:Register , ldp:Container ;
    rdfs:label "Physical quantities - aeronautical meteorology discipline"@en ;
    dct:description "WMO No. 306 Vol I.2 Common Code-table C-15 'Physical quantities - aeronautical meteorology discipline'."@en ;
    reg:owner <http://codes.wmo.int/system/organization/wmo> ;
    reg:manager <http://codes.wmo.int/system/organization/www-dm> ;
    .
    """)
    if not os.path.exists('ttl/common/c-15/me'):
        os.mkdir('ttl/common/c-15/me')
        with open('ttl/common/me/deprec_me.ttl', 'w') as fhandle:
            fhandle.write(ttlhead)
            fhandle.write("""<me>
    a reg:Register , ldp:Container ;
    rdfs:label "Physical quantities - meteorology discipline"@en ;
    dct:description "WMO No. 306 Vol I.2 Common Code-table C-15 'Physical quantities - meteorology discipline'."@en ;
    reg:owner <http://codes.wmo.int/system/organization/wmo> ;
    reg:manager <http://codes.wmo.int/system/organization/www-dm> ;
    .
    """)
    if not os.path.exists('ttl/common/c-15/oc'):
        os.mkdir('ttl/common/c-15/oc')
        with open('ttl/common/oc/deprec_oc.ttl', 'w') as fhandle:
            fhandle.write(ttlhead)
            fhandle.write("""<oc>
    a reg:Register , ldp:Container ;
    rdfs:label "Physical quantities - oceanography discipline"@en ;
    dct:description "WMO No. 306 Vol I.2 Common Code-table C-15 'Physical quantities - oceanography discipline'."@en ;
    reg:owner <http://codes.wmo.int/system/organization/wmo> ;
    reg:manager <http://codes.wmo.int/system/organization/www-dm> ;
    .
    """)
    

    

declared_qk = ['<aerodromeMaximumWindGustSpeed>', '<aerodromeMeanWindDirection>', '<aerodromeMeanWindSpeed>', '<aerodromeMinimumHorizontalVisibility>', '<aerodromeMinimumVisibilityDirection>', '<aeronauticalPrevailingHorizontalVisibility>', '<aeronauticalVisibility>', '<altimeterSettingQnh>', '<depthOfRunwayDeposit>', '<runwayContaminationCoverage>', '<runwayFrictionCoefficient>', '<runwayVisualRangeRvr>', '<seaSurfaceTemperature>', '<airTemperature>', '<atmosphericPressure>', '<dewPointTemperature>', '<heightOfBaseOfCloud>', '<horizontalVisibility>', '<maximumWindGustSpeed>', '<seaSurfaceTemperature>', '<verticalVisibility>']


def make_forward(fname, original, target):
    with open(fname, 'w') as fhandle:
        if target not in declared_qk:
            raise ValueError('{} not a declared quanityt kind'.format(target))
        fhandle.write(ttlhead)
        fandle.write('{} a reg:NamespaceForward , reg:Delegated ;'.format(original))
        fhandle.write('\treg:delegationTarget http://codes.wmo.int/common/quantity-kind/{} ;\n'.format(target))
        fhandle.write('\treg:forwardingCode "301" ;')
        fhandle.write('\t.\n')


redirects = {'ae':[('<cloudDistributionForAviation>',''),
                   ('<significantWeather>',''),
                   ('<significantRecentWeatherPhenomenon>',''),
                   ('<prevailingHorizontalVisibility>','<aeronauticalPrevailingHorizontalVisibility>'),
                   ('<runwayVisualRangeRvr>',''),
                   ('<verticalVisibility>','<verticalVisibility>'),
                   ('<minimumHorizontalVisibility>','<aeronauticalVisibility>'),
                   ('<depthOfRunwayDeposit>','<depthOfRunwayDeposit>'),
                   ('<runwayFrictionCoefficient>','<runwayFrictionCoefficient>'),
                   ('<runwayContamination>','<runwayContaminationCoverage>'),
                   ('<runwayDeposits>','')
                   ],
             'me':[('<dewPointTemperature>',''),
                   ('<airTemperature>',''),
                   ('<uvIndex>',''),
                   ('<horizontalVisibility>','<horizontalVisibility>'),
                   ('<maximumDiameterOfHailstones>',''),
                   ('<windSpeed>',''),
                   ('<windDirection>',''),
                   ('<maximumWindGustSpeed>',''),
                   ('<totalPrecipitationRate>',''),
                   ('<totalPrecipitation>',''),
                   ('<snowDepthWaterEquivalent>',''),
                   ('<totalSnowDepth>',''),
                   ('<pressureTendency>',''),
                   ('<pressureReducedToMeanSeaLevel>',''),
                   ('<geometricHeight>',''),
                   ('<altimeterSettingQnh>','<altimeterSettingQnh>'),
                   ('<heightOfBaseOfCloud>',''),
                   ('<cloudType>',''),
                   ('<meteorologicalFeature>',''),
                   ('<characteristicOfPressureTendency>','')
                   ],
             'oc':[('<seaSurfaceTemperature>',''),
                   ('<seaState>','')
                   ]}

def main():
    make_regs()

if __name__ == '__main__':
    cleanttl.clean()
    main()

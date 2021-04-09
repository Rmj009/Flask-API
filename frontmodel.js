// import { useState, useEffect } from "react";
// import { mean, sampleStandardDeviation } from "simple-statistics";
// import useSpcMeasurePointHistoryGroup from "./spc-measure-point-history-group.hook";


export default function useSpcStatisticsResult(
  spcMeasurePointHistoryData,
  spcMeasurePointConfig
) {
  const [statisticsResult, setStatisticsResult] = useState({
    good: 0,
    defect: 0,
    totalNum: 0,
    goodRate: 0,
    USL: 0,
    LSL: 0,
    UCL: 0,
    LCL: 0,
    sampleStandardDeviation: 0,
    target: 0,
    mean: 0,
    range: 0,
    CPU: 0,
    CPL: 0,
    CP: 0,
    CK: 0,
    CPK: 0,
    PPK: 0,
  });
  const [spcMeasurePointHistoryFormatData] = useSpcMeasurePointHistoryGroup(spcMeasurePointHistoryData,spcMeasurePointConfig)

  // handle statistics result
  useEffect(() => {
    if (spcMeasurePointHistoryFormatData && spcMeasurePointHistoryFormatData.length) {
      // console.log("change data");
      let _min = Number.MAX_SAFE_INTEGER;
      let _max = Number.MIN_SAFE_INTEGER;
      let totalResult = [];
      let totalGroupResult = [];
      spcMeasurePointHistoryFormatData.forEach((data) => {
        totalResult = [
          ...totalResult,
          ...data.valueArray.filter(
            (value) => !(value === -88888888 || value === -99999999)
          ),
        ];
        if (data.value) {
          totalGroupResult = [...totalGroupResult, data.value];
        }
        if (_min > +data.value) {
          _min = +data.value;
        }
        if (_max < +data.value) {
          _max = +data.value;
        }
      });
      // console.log("totalGroupResult");
      // console.log(totalGroupResult);
      // console.log(totalResult);
      if (totalGroupResult.length >= 2 && totalResult.length >= 2) {
        let _statisticsResult = {
          totalNum: totalResult.length,
          USL: +spcMeasurePointConfig.USL + +spcMeasurePointConfig.stdValue,
          LSL: +spcMeasurePointConfig.stdValue - spcMeasurePointConfig.LSL,
          target: +spcMeasurePointConfig.stdValue,
          sampleStandardDeviation: +sampleStandardDeviation(totalResult),
          groupSampleStandardDeviation: +sampleStandardDeviation(
            totalGroupResult
          ),
          mean: mean(totalGroupResult),
        };
        _statisticsResult = {
          ..._statisticsResult,
          range: _statisticsResult.USL - _statisticsResult.LSL, // range range
          good: totalResult.filter(
            (value) =>
              value >= _statisticsResult.LSL && value <= _statisticsResult.USL
          ).length,
          defect: totalResult.filter(
            (value) =>
              value < _statisticsResult.LSL || value > _statisticsResult.USL
          ).length,
          // target: (_statisticsResult.USL+_statisticsResult.LSL)/2,
        };
        _statisticsResult = {
          ..._statisticsResult,
          UCL: (+_statisticsResult.USL + spcMeasurePointConfig.stdValue) / 2,
          LCL: (+_statisticsResult.LSL + +spcMeasurePointConfig.stdValue) / 2,
          goodRate: (_statisticsResult.good / _statisticsResult.totalNum) * 100,
          CK: Math.abs(
            (_statisticsResult.target - _statisticsResult.mean) /
              (_statisticsResult.range / 2)
          ),
          CP: Math.abs(
            _statisticsResult.range /
              (6 * _statisticsResult.groupSampleStandardDeviation)
          ),
        };
        _statisticsResult = {
          ..._statisticsResult,
          CPK: Math.abs((1 - _statisticsResult.CK) * _statisticsResult.CP),
          CPU:
            Math.abs(_statisticsResult.USL - _statisticsResult.mean) /
            (3 * _statisticsResult.groupSampleStandardDeviation),
          CPL:
            Math.abs(_statisticsResult.mean - _statisticsResult.LSL) /
            (3 * _statisticsResult.groupSampleStandardDeviation),
          PPK: Math.abs(
            (1 - _statisticsResult.CK) *
              ((_statisticsResult.USL - _statisticsResult.LSL) /
                (6 * _statisticsResult.sampleStandardDeviation))
          ),
        };
        // console.log(_statisticsResult);
        setStatisticsResult((data) => {
          return {
            ...data,
            ..._statisticsResult,
          };
        });
      }
    } else {
      setStatisticsResult({
        good: 0,
        defect: 0,
        totalNum: 0,
        goodRate: 0,
        USL: 0,
        LSL: 0,
        UCL: 0,
        LCL: 0,
        sampleStandardDeviation: 0,
        target: 0,
        mean: 0,
        range: 0,
        CPU: 0,
        CPL: 0,
        CP: 0,
        CK: 0,
        CPK: 0,
        PPK: 0,
      });
    }
  }, [spcMeasurePointHistoryFormatData, spcMeasurePointConfig]);

  return [statisticsResult];
}

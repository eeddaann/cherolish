# Cherolish
## *open source tremor filtering mouse*
### our database:
<iframe src="https://search-cherolish-elastic-kjxjy7daaejupzxjyv442lvip4.eu-west-1.es.amazonaws.com/_plugin/kibana/app/kibana#/visualize/edit/a55582b0-49d0-11e8-9141-134b6d19df4e?embed=true&_g=()&_a=(filters:!(),linked:!f,query:(language:lucene,query:''),uiState:(),vis:(aggs:!((enabled:!t,id:'1',params:(customLabel:'Number+of+samples'),schema:metric,type:count)),params:(addLegend:!f,addTooltip:!t,metric:(colorSchema:'Green+to+Red',colorsRange:!((from:0,to:10000)),invertColors:!f,labels:(show:!t),metricColorMode:None,percentageMode:!f,style:(bgColor:!f,bgFill:%23000,fontSize:61,labelColor:!f,subText:''),useRanges:!f),type:metric),title:'number+of+samples',type:metric))" height="600" width="800"></iframe>
<iframe src="https://search-cherolish-elastic-kjxjy7daaejupzxjyv442lvip4.eu-west-1.es.amazonaws.com/_plugin/kibana/app/kibana#/visualize/edit/afee2f40-49b9-11e8-9141-134b6d19df4e?embed=true&_g=()&_a=(filters:!(('$state':(store:appState),meta:(alias:!n,disabled:!f,index:cc4a4640-4993-11e8-9141-134b6d19df4e,key:user,negate:!t,params:(query:edan,type:phrase),type:phrase,value:edan),query:(match:(user:(query:edan,type:phrase))))),linked:!f,query:(language:lucene,query:''),uiState:(vis:(defaultColors:('0+-+35':'rgb(0,104,55)','105+-+140':'rgb(166,217,106)','140+-+175':'rgb(217,239,139)','175+-+210':'rgb(255,255,190)','210+-+245':'rgb(254,224,139)','245+-+280':'rgb(253,174,97)','280+-+315':'rgb(244,109,67)','315+-+350':'rgb(214,47,39)','35+-+70':'rgb(26,151,80)','70+-+105':'rgb(102,189,99)'))),vis:(aggs:!((enabled:!t,id:'1',params:(),schema:metric,type:count),(enabled:!t,id:'2',params:(extended_bounds:(),field:x,interval:50),schema:segment,type:histogram),(enabled:!t,id:'3',params:(extended_bounds:(),field:y,interval:50),schema:group,type:histogram)),params:(addLegend:!t,addTooltip:!t,colorSchema:'Green+to+Red',colorsNumber:10,colorsRange:!(),enableHover:!f,invertColors:!f,legendPosition:right,percentageMode:!f,setColorRange:!f,times:!(),type:heatmap,valueAxes:!((id:ValueAxis-1,labels:(color:%23555,rotate:0,show:!f),scale:(defaultYExtents:!f,type:linear),show:!f,type:value))),title:'shaky+mouse+heatmap',type:heatmap))" height="600" width="800"></iframe>

## Installation guide:

### Via Github: 
Type on the terminal:
``` git clone https://github.com/eeddaann/cherolish.git```
Install the required packeges using:
``` pip install -f requirements.txt```
Run using:
``` python main.py```

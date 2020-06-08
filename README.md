<h2>KPI Anomaly Detection</h2>
<h3>Intro</h3>
<ul>
  <li>Data input: Purchase Request numbers along with days taken to process it.</li>
  <li>Methodology: Z-score.</li>
  <li>With Z-score we can define outliers relying on the data background(mean, standard deviation) instead of threshold set up front. Then, we are flexible enough to see what is the standard duration of processing PR and what is beyound the standard.</li>
  <li>Outcome: script returns Puchare Requests numbers that appear as outliers(days above standard duration) and a graph presenting outliers.</li>
  <li>As the following actions leaders can react on time and check what is the reason of processing PR longer than standardised duration.</li>
  <li>Finding the reason enables further analysis in order to imporve the process to avoid similar delays.</li>
</ul>

<h3>Demo</h3>
<img src="images/plot.JPG" width="570" height="500">
<p>Console output:</p>
<img src="images/console.JPG">

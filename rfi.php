<?php
// VICTIM PAGE

echo "<h2>Remote file inclusion test</h2>";
echo "<br>";
echo $_GET["name"];
echo "<br>";
echo $_GET["page"];
echo "<br>";
$malfile= $_GET["page"];
include($malfile); // vulnerability 

?>

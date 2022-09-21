<?php

$url_endpoint='http://127.0.0.1:32000/notepads'

function get_all_records(){
	$url = $url_endpoint;
	$ch = curl_init($url);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
	$output = curl_exec($ch);
	return json_decode($output);
}

function get_metrics(){
	$url = $url_endpoint . '/metrics';
	$ch = curl_init($url);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
	$output = curl_exec($ch);
	return json_decode($output);
}

$all_records = get_all_records();
print_r($all_records);



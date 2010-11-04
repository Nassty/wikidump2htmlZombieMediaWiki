<?php

# Initialise common code
$preIP = dirname( __FILE__ );
require_once( "$preIP/includes/WebStart.php" );

# Initialize MediaWiki base class
require_once( "$preIP/includes/Wiki.php" );
$mediaWiki = new MediaWiki();
include("includes/parser/ParserOptions.php");
include("includes/parser/Parser.php");

$option = new ParserOptions();
$title = new Title();
$parser = new Parser();
$text = ($parser->parse($_REQUEST["text"], $title, $option));
print $text->mText;

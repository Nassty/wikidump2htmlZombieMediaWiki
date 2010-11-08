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
$option->setEditSection(false);
$title = Title::newFromText("set me to something");

$text = ($wgParser->parse(file_get_contents('php://input'), $title, $option));

print $text->getText();

?>

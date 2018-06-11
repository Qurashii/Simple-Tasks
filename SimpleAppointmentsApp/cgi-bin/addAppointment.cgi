#!C:\Strawberry\perl\bin\perl.exe

use strict;
use warnings FATAL => 'all';
use CGI;
use DBI;

print "Content-type: text/html\n\n";

my $driver   = "SQLite";
my $database = "../db/appointment.db";
my $dsn = "DBI:$driver:dbname=$database";
my $userid = "";
my $password = "";
my $dbh = DBI->connect($dsn, $userid, $password, {PrintError => 1, RaiseError => 1, AutoCommit => 1});

my $cgi = CGI->new();

my $date = $cgi->param('date');
my $time = $cgi->param('time');
my $desc = $cgi->param('desc');

$dbh->do('INSERT INTO appointments (app_date, app_time, app_desc) VALUES (?, ?, ?)',
   undef,
   $date, $time , $desc);

$dbh->disconnect();

print"<META HTTP-EQUIV=refresh CONTENT=\"1;URL=http://localhost/AppointmentsApp/\">\n";
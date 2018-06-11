#!C:\Strawberry\perl\bin\perl.exe

use strict;
use warnings;
use CGI;
use DBI;
use JSON;

print "Content-type: text/html\n\n";

my $driver   = "SQLite";
my $database = "../db/appointment.db";
my $dsn = "DBI:$driver:dbname=$database";
my $userid = "";
my $password = "";
my $dbh = DBI->connect($dsn, $userid, $password, {PrintError => 1, RaiseError => 1, AutoCommit => 1});

my $searchText = CGI->new->param('searchText');
my $query;

if ( $searchText eq "" ) {
    $query = qq(SELECT app_date, app_time, app_desc from appointments;);
    $query = $dbh->prepare($query);
} else {
    $query = qq(SELECT app_date, app_time, app_desc from appointments where app_desc LIKE ? ;);
    $query = $dbh->prepare($query);
    $query->bind_param( 1, "%" . $searchText . "%" );
}

my $result = $query->execute() or die $DBI::errstr;

if ( $result < 0 ) {
    print $DBI::errstr;
}

my @output;

while ( my @row = $query->fetchrow_array() ) {
    push(@output, \@row);
}

my $json = JSON->new->utf8;
print $json->encode( \@output ) . "\n";

$dbh->disconnect();
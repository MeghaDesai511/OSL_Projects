use Tk;
use Tk::BrowseEntry;
use strict;
use warnings;

my $mw = MainWindow->new(-title => 'Text Editor');
my $f = $mw->Frame->pack(-side => 'top');

#my $textarea = $mw -> Frame(); #Creating Another Frame
#my $txt = $textarea -> Text(-width=>40, -height=>10);

my @fgColors = (
  'default', 'bold', 'black', 'red', 'blue', 'yellow', 'green',
  'majenta', 'cyan', 'white', 'bold black', 'bold red', 'bold blue',
  'bold yellow', 'bold green', 'bold majenta', 'bold cyan', 'bold whit
+e');

my @bgColors = (
  'default', 'black', 'red', 'blue', 'yellow', 'green', 'majenta', 'cy
+an', 'white');

my %fg = (
  'default'      => "",
  'bold'         => "\e[1m",
  'black'        => "\e[30m",
  'red'          => "\e[31m",
  'blue'         => "\e[32m",
  'yellow'       => "\e[33m",
  'green'        => "\e[34m",
  'majenta'      => "\e[35m",
  'cyan'         => "\e[36m",
  'white'        => "\e[37m",
  'bold black'   => "\e[1;30m",
  'bold red'     => "\e[1;31m",
  'bold blue'    => "\e[1;32m",
  'bold yellow'  => "\e[1;33m",
  'bold green'   => "\e[1;34m",
  'bold majenta' => "\e[1;35m",
  'bold cyan'    => "\e[1;36m",
  'bold white'   => "\e[1;37m",
);

my %bg = (
  'default'      => "",
  'black'        => "\e[40m",
  'red'          => "\e[41m",
  'blue'         => "\e[42m",
  'yellow'       => "\e[43m",
  'green'        => "\e[44m",
  'majenta'      => "\e[45m",
  'cyan'         => "\e[46m",
  'white'        => "\e[47m");

print "                e[40m e[41m e[42m e[43m e[44m e[45m e[46m e[47m
+\n";
foreach my $fgc (@fgColors)
{
  my $printable = $fg{$fgc};
  $printable =~ s/\e/e/;
  printf "%9s ", $printable;

  print "$fg{$fgc}$bg{$_} Text \e[0m" for @bgColors;
  print "\n";
}

$mw->geometry('1000x800');

my $family = 'Courier';
my $be = $f->BrowseEntry(-label => 'Family:', -variable => \$family,
  -browsecmd => \&apply_font)->pack(-fill => 'x', -side => 'left');#->place(-x => 10, -y => 50);
$be->insert('end', sort $mw->fontFamilies);

my $size = 24;
my $bentry = $f->BrowseEntry(-label => 'Size:', -variable => \$size, 
  -browsecmd => \&apply_font)->pack(-side => 'left');#->place(-x => 30, -y => 50);
$bentry->insert('end', (3 .. 32));

my $weight = 'normal';
$f->Checkbutton(-onvalue => 'bold', -offvalue => 'normal', 
  -text => 'Weight', -variable => \$weight, 
  -command => \&apply_font)->pack(-side => 'left');#->place(-x => 50, -y => 50);

my $slant = 'roman';
$f->Checkbutton(-onvalue => 'italic', -offvalue => 'roman', 
  -text => 'Slant', -variable => \$slant, 
  -command => \&apply_font)->pack(-side => 'left');#->place(-x => 100, -y => 70);

my $underline = 0;
$f->Checkbutton(-text => 'Underline', -variable => \$underline, 
  -command => \&apply_font)->pack(-side => 'left');#->place(-x => 100, -y => 90);

my $overstrike = 0; 
$f->Checkbutton(-text => 'Overstrike', -variable => \$overstrike, 
  -command => \&apply_font)->pack(-side => 'left');#->place(-x => 100, -y => 110);

my $stext = 'Sample Text';


my $scroll = $mw->Scrollbar(-orient => "horizontal", -width => 30 ); # create Scrollbar

my $sample = $mw->Entry(-textvariable => \$stext,-xscrollcommand => [ 'set' => $scroll ])->pack(-fill => 'x')->place(-relx =>0.30, -y => 50, -width => 500 , -height => 500);

$scroll->pack(-expand => 1, -fill => 'x')->place(-relx => 0.3, -y => 550, -width =>500);
$scroll->configure(-command => [ $sample => 'xview' ]); # link them




#$textarea -> grid(-row=>5,-column=>1,-columnspan=>2);

&apply_font;

MainLoop;

sub apply_font {
  # Specify all options for font in an anonymous array
  $sample->configure(-font => 
    [-family => $family,
     -size => $size,
     -weight => $weight,
     -slant => $slant,
     -underline => $underline,
     -overstrike => $overstrike]);
}

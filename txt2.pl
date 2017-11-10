use Tk;
use Tk::BrowseEntry;
use strict;

my $mw = MainWindow->new(-title => 'Text Editor');
my $f = $mw->Frame->pack(-side => 'top');

#my $textarea = $mw -> Frame(); #Creating Another Frame
#my $txt = $textarea -> Text(-width=>40, -height=>10);

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
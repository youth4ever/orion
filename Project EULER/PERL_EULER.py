
###################### Counting rectangles     -       Problem 85 ###########################
# Sat, 20 Aug 2016, 14:17       PB085
# trizen

# Using binomials:
use 5.010;
use ntheory qw(binomial);

my $t = 2_000_000;
my $m = 'inf';
my $v = [0, 0];

my ($x, $y) = (int(sqrt($t)), 1);

while (1) {
    my $p = binomial($x + 1, 2) * binomial($y + 1, 2);
    my $d = abs($p - $t);

    if ($d < $m) {
        $v = [$x, $y];
        $m = $d;
    }

    $x >= $y ? ($p > $t ? --$x : ++$y) : last;
}

say "(@{$v}) = ", $v->[0] * $v->[1];

################################# PB 094 Almost equilateral triangles        -       Problem 94
# Wed, 17 Aug 2016, 19:12
# trizen
# Using two closed-form expressions to calculate each side x in (x, x, x+1) and y in (y, y, y-1).

use 5.010;
use strict;
use warnings;

my $n     = 1;
my $sum   = 0;
my $limit = 1_000_000_000;

while (1) {
    my $x = (((7 - 4 * sqrt(3))**$n)
            + (7 + 4 * sqrt(3))**$n + 1) / 3;

    my $y = ((sqrt(3) + 2) * (7 - 4 * sqrt(3))**($n + 1)
           - (sqrt(3) - 2) * (7 + 4 * sqrt(3))**($n + 1) - 1) / 3;

    my $p1 = 3 * $x + 1;
    my $p2 = 3 * $y - 1;

    last if ($p1 > $limit and $p2 > $limit);

    $sum += $p1 if $p1 <= $limit;
    $sum += $p2 if $p2 <= $limit;

    ++$n;
}

say $sum;

#################################PB 064 Odd period square roots ##########################
# trizen , Wed, 31 Aug 2016, 17:35

use 5.010;
use strict;

use ntheory qw(is_power sqrtint);

sub period_length {
    my ($n) = @_;

    my $x = sqrtint($n);
    my $y = $x;
    my $z = 1;

    my $period = 0;

    do {
        $y = int(($x + $y) / $z) * $z - $y;
        $z = int(($n - $y * $y) / $z);
        ++$period;
    } until (($y == $x) && ($z == 1));

    $period;
}

my $count = 0;
for my $i (1 .. 10000) {
    if (!is_power($i, 2)) {
        ++$count if period_length($i) % 2 != 0;
    }
}

say $count;


############################## PB095 - Amicable Chains ######################
# Sun, 9 Oct 2016, 22:07  ,   trizen

use 5.010;
use strict;
use ntheory qw(divisor_sum);

my $limit = 1e6;

my %chain;
foreach my $n (1 .. $limit) {
    my $len  = 0;
    my $orig = $n;

    my %seen;
    while (1) {
        my $sum = divisor_sum($n) - $n;
        last if $seen{$sum}++;
        last if $sum > $limit;
        $n = $sum;
        ++$len;
    }

    if (exists $seen{$orig}) {
        $chain{$len} //= $orig;
    }
}

say $chain{(sort { $b <=> $a } keys %chain)[0]};

################################# PB061 - CYCLICAL FIGURATE NUMBERS ###############
#Tue, 16 Aug 2016, 21:58, trizen


use 5.010;
use strict;
use warnings;

use ntheory qw(forperm);
use List::Util qw(sum);

sub quadratic_formula {
    my ($x, $y, $z) = @_;
    (-$y + sqrt($y**2 - 4 * $x * $z)) / (2 * $x);
}

#
## Generation
#

sub triangle {
    $_[0] * ($_[0] + 1) / 2;
}

sub square {
    $_[0] * $_[0];
}

sub pentagon {
    $_[0] * (3 * $_[0] - 1) / 2;
}

sub hexagon {
    $_[0] * (2 * $_[0] - 1);
}

sub heptagon {
    $_[0] * (5 * $_[0] - 3) / 2;
}

sub octagon {
    $_[0] * (3 * $_[0] - 2);
}

#
## Roots
#

sub triangle_root {
    quadratic_formula(1 / 2, 1 / 2, -$_[0]);
}

sub square_root {
    quadratic_formula(1, 0, -$_[0]);
}

sub pentagon_root {
    quadratic_formula(3 / 2, -1, -$_[0]);
}

sub hexagon_root {
    quadratic_formula(2, -1, -$_[0]);
}

sub heptagon_root {
    quadratic_formula(5 / 2, -3 / 2, -$_[0]);
}

sub octagon_root {
    quadratic_formula(3, -2, -$_[0]);
}

#
## Validation
#

sub is_triangle {
    triangle(int(triangle_root($_[0]))) == $_[0];
}

sub is_square {
    square(int(square_root($_[0]))) == $_[0];
}

sub is_pentagon {
    pentagon(int(pentagon_root($_[0]))) == $_[0];
}

sub is_hexagon {
    hexagon(int(hexagon_root($_[0]))) == $_[0];
}

sub is_heptagon {
    heptagon(int(heptagon_root($_[0]))) == $_[0];
}

sub is_octagon {
    octagon(int(octagon_root($_[0]))) == $_[0];
}

my @range = grep { substr($_, 2, 1) ne '0' } 1000 .. 9999;

my (%trig, %square, %penta, %hexa, %hepta, %octa);

foreach my $n (@range) {
    my ($h, $t) = (substr($n, 0, 2), substr($n, -2));
    is_triangle($n) && undef $trig{$h}{$t};
    is_square($n)   && undef $square{$h}{$t};
    is_pentagon($n) && undef $penta{$h}{$t};
    is_hexagon($n)  && undef $hexa{$h}{$t};
    is_heptagon($n) && undef $hepta{$h}{$t};
    is_octagon($n)  && undef $octa{$h}{$t};
}

my (@a) = (\%trig, \%square, \%penta, \%hexa, \%hepta, \%octa);

forperm {
    my @h = @a[@_];

    foreach my $ah (keys %{$h[0]}) {
        foreach my $at (keys %{$h[0]{$ah}}) {
            foreach my $bt (keys %{$h[1]{$at}}) {
                foreach my $ct (keys %{$h[2]{$bt}}) {
                    foreach my $dt (keys %{$h[3]{$ct}}) {
                        foreach my $et (keys %{$h[4]{$dt}}) {
                            if (exists $h[5]{$et}{$ah}) {
                                my @nums = split(' ', "$ah$at $at$bt $bt$ct $ct$dt $dt$et $et$ah");
                                say "sum(@nums) = ", sum(@nums);
                            }
                        }
                    }
                }
            }
        }
    }

} scalar(@a);

############################   PB066 - DIOPHANTINE EQUATION  ####
# Wed, 31 Aug 2016, 21:18 , trizen
use 5.010;
use strict;
use warnings;

use Math::BigNum qw(:constant);
use ntheory qw(is_power sqrtint);

sub sqrt_convergents {
    my ($n) = @_;

    my $x = sqrtint($n);
    my $y = $x;
    my $z = 1;

    my @convergents = ($x);

    do {
        $y = int(($x + $y) / $z) * $z - $y;
        $z = int(($n - $y * $y) / $z);
        push @convergents, int(($x + $y) / $z);
    } until (($y == $x) && ($z == 1));

    return @convergents;
}

sub continued_frac {
    my ($i, $c) = @_;
    $i->is_neg ? 0 : ($c->[$i] + continued_frac($i - 1, $c))->binv;
}

sub solve {
    my ($d) = @_;

    my ($k, @c) = sqrt_convergents($d);

    my @period = @c;
    for (my $i = 0 ; ; ++$i) {
        if ($i > $#c) { push @c, @period; $i = 2 * $i - 1 }
        my $x = continued_frac($i, [$k, (@c) x ($i + 1)])->denominator;
        return $x if is_power(4 * $d * ($x*$x - 1), 2);
    }
}

my %max = (x => 0, d => -1);

foreach my $i (2 .. 1000) {
    is_power($i, 2) && next;

    my $x = solve($i);

    if ($x > $max{x}) {
        $max{x} = $x;
        $max{d} = $i;
    }
}

say $max{d};

############################  PB131 - Prime-Cube Partnership  ########
# Thu, 21 Apr 2016, 16:49,   trizen
# General formula: n^9 + n^6 * p = (n^3 + n^2)^3 where p is a prime number.
# From the above formula results that p must have the form: 3n^2 + 3n + 1.

use integer;
use ntheory qw(is_prime);

my $count = 0;

for(my $n = 1; ; $n++) {
    my $p = 3*$n**2 + 3*$n + 1;
    last if $p >= 1e6;
    ++$count if is_prime($p);
}

print "$count\n";

##############################   PB077 - Prime Summations, Prime Partitions      #########################
# Sat, 14 Nov 2015, 19:42 , trizen
# Pretty simple algorithm in Perl:

use 5.010;
use strict;
use warnings;
use ntheory qw(primes);
use List::Util qw(sum0);

sub count {
    my ($n, $primes, $solution) = @_;
    my $sum = sum0(@$solution);

    ($sum == $n)                 ? 1
    : ($sum > $n || !@{$primes}) ? 0
    : (count($n, $primes, [@{$solution}, $primes->[0]]) +
       count($n, [@{$primes}[1 .. $#{$primes}]], $solution));
}

foreach my $i (4 .. 1e6) {
    if (count($i, primes(1, $i - 2), []) > 5000) {
        say $i; last;
    }
}


# Optimized solution:
use 5.010;
use strict;
use warnings;
use ntheory qw(primes);
use Memoize qw(memoize);

my $primes;

sub count {
    my ($n, $i, $sum) = @_;

    ($sum == $n)                      ? 1
    : ($sum > $n || $i > $#{$primes}) ? 0
    : (count($n, $i, $sum + $primes->[$i]) +
       count($n, $i+1, $sum))
}

memoize('count');

foreach my $i (4 .. 1e6) {
    $primes = primes(1, $i - 2);
    if (count($i, 0, 0) > 5000) {
        say $i; last;
    }
}


##############################    PB079 Passcode Derivation     #########################
Wed, 14 Sep 2016, 17:06,  onime
open(my $fh,'<',"passcode_keylog.txt");
my @log = <$fh>;
my @passcode = qw/0 1 2 3 6 7 8 9/;

foreach my $code (@log)
{
    chomp($code);

    my @digits = split(//,$code);
    my @pos = sort map( index(join("",@passcode),$_), @digits);

    $passcode[$_] = shift @digits foreach(@pos);
}

print @passcode;


##############################  pb112 -   Bouncy numbers      #########################
# Mon, 8 Aug 2016, 17:22, trizen

use List::Util qw(all);

sub is_bouncy {
    !(
          (all { $_[$_ - 1] <= $_[$_] } 1 .. $#_)
       || (all { $_[$_ - 1] >= $_[$_] } 1 .. $#_)
    );
}

my $n = 1;
my $count = 0;

while (1) {
    is_bouncy(split(//, $n)) && ++$count;

    if ($count / $n * 100 == 99) {
        print "$n\n";
        last;
    }

    ++$n;
}

##############################         #########################
# Sun, 7 Aug 2016, 23:31,  trizen ;   Brute-force solution in Perl, using `eval()` (runs in ~13 sec):

use ntheory qw(forperm);

my @op = ('+', '-', '*', '/');

my @expr = (
            "%d %s %d %s %d %s %d",
            "%d %s (%d %s (%d %s %d))",
            "%d %s ((%d %s %d) %s %d)",
            "(%d %s (%d %s %d)) %s %d",
            "%d %s (%d %s %d %s %d)",
            "%d %s (%d %s %d) %s %d",
            "%d %s %d %s (%d %s %d)",
            "((%d %s %d) %s %d) %s %d",
            "(%d %s %d) %s (%d %s %d)",
           );

sub evaluate {
    my ($nums, $ops, $table) = @_;
    foreach my $expr (@expr) {

        my $n = eval sprintf($expr,
            $nums->[0], $ops->[0],
            $nums->[1], $ops->[1],
            $nums->[2], $ops->[2],
            $nums->[3]
        );

        if (not $@
            and $n > 0
            and int($n) eq $n
            and not exists $table->{$n}) {
            undef $table->{$n};
        }
    }
}

sub compute {
    my ($set, $table) = @_;

    forperm {
        my @nums = @{$set}[@_];

        foreach my $i (0 .. 3) {
            foreach my $j (0 .. 3) {
                foreach my $k (0 .. 3) {
                    my @ops = @op[$i, $j, $k];
                    evaluate(\@nums, \@ops, $table);
                }
            }
        }

    } scalar(@$set);
}

my %max;

foreach my $i (1 .. 9) {
    foreach my $j ($i + 1 .. 9) {
        foreach my $k ($j + 1 .. 9) {
            foreach my $l ($k + 1 .. 9) {
                compute([$i, $j, $k, $l], \my %table);

                my ($n, $c) = (0, 0);
                my @keys = sort { $a <=> $b } keys %table;

                while (@keys) {
                    shift(@keys) == ++$n ? ++$c : last;
                }

                if ($c > ($max{max} || 0)) {
                    $max{max} = $c;
                    $max{set} = [$i, $j, $k, $l];
                }
            }
        }
    }
}

print "$max{max}: [@{$max{set}}]\n";


##############################   PB123 Prime Square Remainders     #########################
# Wed, 17 Aug 2016, 00:47,   trizen
# Trivial when combined with modular exponentiation (run-time: ~100 ms):

use 5.010;
use ntheory qw(nth_prime powmod);

my $n = 7037;

while (1) {
    my $p = nth_prime(++$n);
    my $s = $p * $p;
    my $r = (powmod($p - 1, $n, $s) + powmod($p + 1, $n, $s)) % $s;

    if ($r > 10**10) {
        say $n;
        last;
    }
}

##############################   PB146 - Investigating Prime Pattern      #########################
# Wed, 28 Oct 2015, 19:33 , trizen
# 15 seconds in Perl, using the "ntheory" library.

use 5.010;
use strict;
use integer;
use ntheory qw(is_prime next_prime);

my $sum = 0;
for (my $i = 10; $i < 150_000_000; $i += 10) {
    my $x = $i**2;
    if (    is_prime($x + 1)
        and next_prime($x + 1) == $x + 3
        and next_prime($x + 3) == $x + 7
        and next_prime($x + 7) == $x + 9
        and next_prime($x + 9) == $x + 13
        and next_prime($x + 13) == $x + 27) {
        $sum += $i;
    }
}
say $sum;

##############################         #########################
##############################         #########################
##############################         #########################
##############################         #########################
##############################         #########################
##############################         #########################
##############################         #########################
##############################         #########################
##############################         #########################
##############################         #########################
##############################         #########################
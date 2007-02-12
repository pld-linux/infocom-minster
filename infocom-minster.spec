%define		_name		minster
Summary:	Infocom text game - Christminster
Summary(pl.UTF-8):   Tekstówka Infocomu - Christminster
Name:		infocom-minster
Version:	961117
Release:	2
License:	free
Group:		Applications/Games
Source0:	ftp://ftp.ifarchive.org/if-archive/games/zcode/%{_name}.z5
# Source0-md5:	e343b97402ea4220bf19bb3fe39ae008
URL:		http://www.ifarchive.org/
Requires:	zcode-wrapper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%description
When your brother Malcolm sends you a telegram inviting you to visit
him at Biblioll College in the ancient university town of
Christminster, you imagine that the mysterious `discovery' he alludes
to is nothing more than some esoteric bit of chemistry, and that
you'll have a pleasant day out in beautiful surroundings.

But when you get to Christminster, nothing is as you expect. Where has
Malcolm vanished to? What are the unpleasant Doctor Jarboe and the
positively repulsive Professor Bungay up to? And what do
long-forgotten alchemical treatises have to do with the modern day?

%description -l pl.UTF-8
Gdy twój brat Malcolm wysyła ci telegram zapraszający do odwiedzenia
go w Biblioll College w starożytnym miasteczku uniwersyteckim
Christminster, wyobrażasz sobie, że tajemnicze ,,odkrycie'', o którym
ci napomknął nie jest niczym innym niż ezoterycznym kawałkiem chemii i
w związku z tym spędzisz miły dzień w pięknym otoczeniu.

Ale gdy docierasz do Christminster, nic nie dzieje się zgodnie z
przewidywaniami. Gdzie zniknął Malcolm? Co się dzieje z niemiłym
doktorem Jarboe i ze zdecydowanie odpychającym profesorem Bungayem?
Oraz co robią w czasach współczesnych dawno zapomniane rozprawy
alchemiczne?

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/games/zcode}

cp %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/games/zcode
ln -s %{_datadir}/games/zcode/wrapper.sh $RPM_BUILD_ROOT%{_bindir}/%{_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/games/zcode/*.z5

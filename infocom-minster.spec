%define		_name		minster
Summary:	Infocom text game - Christminster
Summary(pl):	Tekstówka Infocomu - Christminster
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

%description -l pl
Gdy twój brat Malcolm wysy³a ci telegram zapraszaj±cy do odwiedzenia
go w Biblioll College w staro¿ytnym miasteczku uniwersyteckim
Christminster, wyobra¿asz sobie, ¿e tajemnicze ,,odkrycie'', o którym
ci napomkn±³ nie jest niczym innym ni¿ ezoterycznym kawa³kiem chemii i
w zwi±zku z tym spêdzisz mi³y dzieñ w piêknym otoczeniu.

Ale gdy docierasz do Christminster, nic nie dzieje siê zgodnie z
przewidywaniami. Gdzie znikn±³ Malcolm? Co siê dzieje z niemi³ym
doktorem Jarboe i ze zdecydowanie odpychaj±cym profesorem Bungayem?
Oraz co robi± w czasach wspó³czesnych dawno zapomniane rozprawy
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

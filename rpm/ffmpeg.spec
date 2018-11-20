Name:           ffmpeg
Version:        3.4.9999
Release:        1
Summary:        FFmpeg video encoding and decoding library
Group:          Productivity/Multimedia/Video/Editors and Convertors
Url:            http://ffmpeg.org/
Source:         http://ffmpeg.org/releases/%{name}-%{version}.tar.bz2
License:        LGPLv2.1+
BuildRequires:  pkgconfig(speex)
Conflicts:      libav
%ifarch i486 x86_64
BuildRequires:  yasm
%endif

%description
FFmpeg: a complete, cross-platform solution to record, convert and stream audio and video. 

%package devel
Summary:        FFmpeg development package
Requires:       %{name} = %{version}
Requires:       bzip2-devel
Conflicts:      libav-devel

%description devel
Development headers and libraries for FFmpeg - a complete, cross-platform solution to record, convert and stream audio and video. 

%package tools
Summary:        FFmpeg tools package
Requires:       %{name} = %{version}
Conflicts:      libav-tools

%description tools
Development tools for FFmpeg - a complete, cross-platform solution to record, convert and stream audio and video. 

%prep
%setup -q -n %{name}-%{version}/upstream

%build
./configure --prefix=/usr --disable-debug --enable-shared --enable-pic \
  --disable-static --disable-doc --disable-muxers --disable-demuxers --disable-protocols \
  --disable-indevs --disable-outdevs --disable-avdevice --disable-network \
  --disable-lsp --disable-hwaccels --disable-encoders --disable-decoders --disable-bsfs \
  --enable-protocol=file --enable-fft --enable-decoder=aac --enable-decoder=aac_latm \
  --enable-decoder=vorbis --enable-decoder=theora --enable-decoder=flac \
  --enable-encoder=aac --enable-demuxer=aac --enable-demuxer=avi --enable-demuxer=flac \
  --enable-demuxer=h264 --enable-demuxer=m4v --enable-demuxer=mov --enable-demuxer=ogg \
  --enable-demuxer=mpegts --enable-demuxer=mpegvideo --enable-demuxer=matroska \
  --enable-demuxer=wav --enable-decoder=h264 --enable-decoder=mpeg4 --enable-decoder=mp3 \
  --enable-demuxer=aiff --enable-demuxer=flv --enable-demuxer=mjpeg \
  --enable-decoder=pcm_u8 --enable-decoder=pcm_u32le --enable-decoder=pcm_u32be \
  --enable-decoder=pcm_u24le --enable-decoder=pcm_u24be --enable-decoder=pcm_u16le \
  --enable-decoder=pcm_u16be --enable-decoder=pcm_s8 --enable-decoder=pcm_s32le \
  --enable-decoder=pcm_s32be --enable-decoder=pcm_s24le --enable-decoder=pcm_s24be \
  --enable-decoder=pcm_s16le --enable-decoder=pcm_s16be --enable-decoder=pcm_f64le \
  --enable-decoder=pcm_f64be --enable-decoder=pcm_f32le --enable-decoder=pcm_f32be \
  --enable-demuxer=pcm_u32be --enable-demuxer=pcm_u32le --enable-demuxer=pcm_u8 \
  --enable-demuxer=pcm_alaw --enable-demuxer=pcm_f32be --enable-demuxer=pcm_f32le \
  --enable-demuxer=pcm_f64be --enable-demuxer=pcm_f64le --enable-demuxer=pcm_s16be \
  --enable-demuxer=pcm_s16le --enable-demuxer=pcm_s24be --enable-demuxer=pcm_s24le \
  --enable-demuxer=pcm_s32be --enable-demuxer=pcm_s32le --enable-demuxer=pcm_s8 \
  --enable-demuxer=pcm_u16be --enable-demuxer=pcm_u16le --enable-demuxer=pcm_u24be \
  --enable-demuxer=pcm_u24le --enable-decoder=mjpeg --enable-decoder=vp8 --enable-decoder=vp9 \
  --enable-libspeex --enable-decoder=opus
  
#./configure --prefix=/usr --disable-debug --enable-shared --enable-pic \
#  --disable-programs --disable-doc --disable-everything --enable-protocol=file \
#  --enable-libopus --enable-decoder=aac --enable-decoder=aac_latm --enable-decoder=aasc \
#  --enable-decoder=flac --enable-decoder=gif --enable-decoder=h264 --enable-decoder=h264_vdpau \
#  --enable-decoder=mp1 --enable-decoder=mp1float --enable-decoder=mp2 \
#  --enable-decoder=mp2float --enable-decoder=mp3 --enable-decoder=mp3adu \
#  --enable-decoder=mp3adufloat --enable-decoder=mp3float --enable-decoder=mp3on4 \
#  --enable-decoder=mp3on4float --enable-decoder=mpeg4 --enable-decoder=mpeg4_vdpau \
#  --enable-decoder=msmpeg4v2 --enable-decoder=msmpeg4v3 --enable-decoder=opus \
#  --enable-decoder=pcm_alaw --enable-decoder=pcm_alaw_at --enable-decoder=pcm_f32be \
#  --enable-decoder=pcm_f32le --enable-decoder=pcm_f64be --enable-decoder=pcm_f64le \
#  --enable-decoder=pcm_lxf --enable-decoder=pcm_mulaw --enable-decoder=pcm_mulaw_at \
#  --enable-decoder=pcm_s16be --enable-decoder=pcm_s16be_planar --enable-decoder=pcm_s16le \
#  --enable-decoder=pcm_s16le_planar --enable-decoder=pcm_s24be --enable-decoder=pcm_s24daud \
#  --enable-decoder=pcm_s24le --enable-decoder=pcm_s24le_planar --enable-decoder=pcm_s32be \
#  --enable-decoder=pcm_s32le --enable-decoder=pcm_s32le_planar --enable-decoder=pcm_s64be \
#  --enable-decoder=pcm_s64le --enable-decoder=pcm_s8 --enable-decoder=pcm_s8_planar \
#  --enable-decoder=pcm_u16be --enable-decoder=pcm_u16le --enable-decoder=pcm_u24be \
#  --enable-decoder=pcm_u24le --enable-decoder=pcm_u32be --enable-decoder=pcm_u32le \
#  --enable-decoder=pcm_u8 --enable-decoder=pcm_zork --enable-decoder=vorbis \
#  --enable-decoder=wavpack --enable-decoder=wmalossless --enable-decoder=wmapro \
#  --enable-decoder=wmav1 --enable-decoder=wmav2 --enable-decoder=wmavoice --enable-encoder=libopus \
#  --enable-hwaccel=h264_vaapi --enable-hwaccel=h264_vdpau --enable-hwaccel=mpeg4_vaapi \
#  --enable-hwaccel=mpeg4_vdpau --enable-parser=aac --enable-parser=aac_latm --enable-parser=flac \
#  --enable-parser=h264 --enable-parser=mpeg4video --enable-parser=mpegaudio --enable-parser=opus \
#  --enable-parser=vorbis --enable-demuxer=aac --enable-demuxer=flac --enable-demuxer=gif \
#  --enable-demuxer=h264 --enable-demuxer=mov --enable-demuxer=mp3 --enable-demuxer=ogg \
#  --enable-demuxer=wav --enable-muxer=ogg --enable-muxer=opus

make %{?_smp_mflags}

%install
# Remove examples
%make_install
rm -rf $RPM_BUILD_ROOT/%{_datadir}/%{name}/examples

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_datadir}/ffmpeg/*.ffpreset
%{_datadir}/ffmpeg/ffprobe.xsd
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root)
%{_libdir}/*.so
%{_includedir}/libavcodec/*.h
%{_includedir}/libavfilter/*.h
%{_includedir}/libavformat/*.h
%{_includedir}/libavutil/*.h
%{_includedir}/libswscale/*.h
%{_includedir}/libswresample/*.h
%{_libdir}/pkgconfig/*.pc

%files tools
%defattr(-,root,root)
%{_bindir}/ffmpeg
%{_bindir}/ffprobe
#%{_bindir}/ffserver

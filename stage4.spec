subarch: amd64
target: stage4
version_stamp: systemd-latest
rel_type: default
profile: default/linux/amd64/13.0/desktop/plasma/systemd
snapshot: latest
source_subpath: default/stage3-amd64-latest
portage_confdir: /data/GitHub/mine/packaging/catalyst/portage

stage4/use:
	bash-completion
	bindist
	bzip2
	idm
	ipv6
	mmx
	sse
	sse2
	urandom

stage4/packages:
	app-admin/logrotate
	app-admin/sudo
	app-admin/syslog-ng
	app-editors/vim
	app-emulation/cloud-init
	app-portage/eix
	app-portage/gentoolkit
	app-portage/layman
	dev-vcs/git
	net-misc/dhcpcd
	net-misc/iputils
	net-misc/networkmanager
	net-wireless/broadcom-sta
	sys-boot/grub
	sys-apps/dmidecode
	sys-apps/gptfdisk
	sys-apps/iproute2
	sys-apps/lsb-release
	sys-apps/pciutils
	sys-block/parted
	sys-devel/bc
	sys-power/acpid
	sys-process/cronie
stage4/fsscript: /data/GitHub/mine/packaging/catalyst
stage4/root_overlay: /data/GitHub/mine/packaging/catalyst/gentoo-stage4
stage4/rcadd:
	acpid|default
	cloud-config|default
	cloud-final|default
	cloud-init-local|default
	cloud-init|default
	cronie|default
	dhcpcd|default
	net.lo|default
	netmount|default
	sshd|default
	syslog-ng|default

boot/kernel: gentoo
boot/kernel/gentoo/sources: gentoo-sources
boot/kernel/gentoo/config: /data/GitHub/mine/packaging/catalyst/gentoo-stage4/etc/kernels/config-4.10.10-gentoo 
boot/kernel/gentoo/extraversion: openstack
boot/kernel/gentoo/gk_kernargs: --all-ramdisk-modules

# all of the cleanup...
stage4/unmerge:
	sys-kernel/genkernel
	sys-kernel/gentoo-sources

stage4/empty:
	/root/.ccache
	/tmp
	/usr/portage/distfiles
	/usr/src
	/var/cache/edb/dep
	/var/cache/genkernel
  /var/cache/portage/distfiles
	/var/empty
	/var/run
	/var/state
	/var/tmp

stage4/rm:
	/etc/*-
	/etc/*.old
	/etc/ssh/ssh_host_*
	/root/.*history
	/root/.lesshst
	/root/.ssh/known_hosts
	/root/.viminfo
	# Remove any generated stuff by genkernel
	/usr/share/genkernel
	# This is 3MB of crap for each copy
	/usr/lib64/python*/site-packages/gentoolkit/test/eclean/testdistfiles.tar.gz

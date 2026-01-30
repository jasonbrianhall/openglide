#!/bin/bash
tar czf ~/rpmbuild/SOURCES/openglide-0.09.tar.gz --exclude-vcs --exclude='*.o' --exclude='*.lo' --exclude='.libs' --exclude='*.la' --exclude='redhat-linux-build' --transform='s,^,openglide-0.09/,' .

# Run rpmbuild
echo ""
echo "Running rpmbuild..."
rpmbuild -ba openglide.spec

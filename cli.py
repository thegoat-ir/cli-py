import whois
import argparse

def cmd_whois(args):
    domain = args['<domain>']
    as_json = args['json']
    w = whois.whois(domain, as_json)
    w.lookup()
    if as_json:
        print(w.json)
    else:
        print(w.text)

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(title='Commands', dest='command')

    ##################
    #### Commands ####
    ##################

    # whois
    whois_parser = subparsers.add_parser('whois', help='whois <domain>')
    whois_parser.add_argument('<domain>', type=str, help='domain to lookup')
    whois_parser.add_argument('-j', '--json', help='print as json', action='store_true')

    commands = {
        'whois': cmd_whois,
    }

    args = vars(parser.parse_args())
    commands[args['command']](args)
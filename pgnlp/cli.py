import argparse
from pprint import pprint

from pgnlp.preprocessing import Pipeline
from pgnlp.metrics import count_words

def arg_parser():
    parser = argparse.ArgumentParser(prog ='nlpcli', 
                                     description ='CLI for Internals package.')

    parser.add_argument('-t', '--texts', type=str, required=False, default='', dest='texts',
                        help="texts to process (Single text OR File)")

    parser.add_argument("--processes", dest="processes", action="store_true", 
                        help="Will print all available processes")

    parser.add_argument("--lowercase", dest="lowercase", action="store_true", 
                        help="Will lowercase texts")

    parser.add_argument("--remove_numbers", dest="remove_numbers", action="store_true", 
                        help="Will remove numbers")

    parser.add_argument("--remove_punctuations", dest="remove_punctuations", action="store_true", 
                        help="Will remove punctuations")

    parser.add_argument("--remove_urls", dest="remove_urls", action="store_true", 
                        help="Will remove urls")

    parser.add_argument("--remove_user_mentions", dest="remove_user_mentions", action="store_true", 
                        help="Will remove user_mentions")

    parser.add_argument("--remove_hashtags", dest="remove_hashtags", action="store_true", 
                        help="Will remove hashtags")

    parser.add_argument("--remove_dates", dest="remove_dates", action="store_true", 
                        help="Will remove dates")

    parser.add_argument("--remove_emoji", dest="remove_emoji", action="store_true", 
                        help="Will remove emoji")

    parser.add_argument("--remove_stopwords", dest="remove_stopwords", action="store_true", 
                        help="Will remove stopwords")

    return parser.parse_args()

def main():
    args = arg_parser()
    texts = args.texts
    processes = args.processes
    lowercase = args.lowercase

    if processes is True:
        pass
    
    else:
        template = []
        append = template.append
        for k, v in args.__dict__.items():
            if k not in ['texts', 'processes', 'lowercase']:
                if v is True:
                    append(k)
        pipe = Pipeline(template=template)
        pprint(pipe.execute(texts=texts, lowercase=lowercase))
        
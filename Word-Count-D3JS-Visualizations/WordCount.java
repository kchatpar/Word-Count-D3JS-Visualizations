import java.io.IOException;
import java.util.StringTokenizer;
import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class WordCount {

  public static class TokenizerMapper
       extends Mapper<Object, Text, Text, IntWritable>{

    private final static IntWritable one = new IntWritable(1);
    private Text word = new Text();

    public void map(Object key, Text value, Context context
                    ) throws IOException, InterruptedException {
	    
      String value2 = value.toString();
      value2  = value2.replaceAll("[^a-zA-Z]+"," ");  //removing special characters

       StringTokenizer itr2 = new StringTokenizer(value2);
      String value3="";
	while(itr2.hasMoreTokens())            //removing stop words.    
	{
		String cmp=itr2.nextToken().toString();
			 if(check(cmp))
		        {
		          value3+=cmp+" ";
		        }

	}

      StringTokenizer itr = new StringTokenizer(value3);
      while (itr.hasMoreTokens()) {
        word.set(itr.nextToken());
        context.write(word, one);
      }
    }

  static Boolean check(String cmp)
    {
      String[] stopwords = {"a","about","above","after","again","against","all","am","an","and","any",
				"are","as","at","be","because","been","before","being","below","between","both","but",
				"by","could","did","do","does","doing","down","during","each","few","for","from",
				"further","had","has","have","having","he","he’d","he’ll","he’s","her","here",
				"here’s","hers","herself","him","himself","his","how","how’s","I","I’d","I’ll","I’m",
				"I’ve","if","in","into","is","it","it’s","its","itself","let’s","me","more","most","my","myself",
				"nor","of","on","once","only","or","other","ought","our","ours","ourselves","out","over","own","same","she","she’d","she’ll",
				"she’s","should","so","some","such","than","that","that’s","the","their","theirs","them",
				"themselves","then","there","there’s","these","they","they’d","they’ll","they’re","they’ve","this","those","through","to","too","under","until","up","very",
				"was","we","we’d","we’ll","we’re","we’ve","were","what","what’s","when",
				"when’s","where","where’s","which","while","who","who’s","whom","why",
				"why’s","with","would","you","you’d","you’ll","you’re","you’ve","your","yours","yourself","yourselves"};
	for(String s:stopwords)
	{
		if(cmp.equals(s))
		{
			return false;
		}
	}
	return true;
    }
  }

  public static class IntSumReducer
       extends Reducer<Text,IntWritable,Text,IntWritable> {
    private IntWritable result = new IntWritable();

    public void reduce(Text key, Iterable<IntWritable> values,
                       Context context
                       ) throws IOException, InterruptedException {
      int sum = 0;
      for (IntWritable val : values) {
        sum += val.get();
      }
      result.set(sum);
      context.write(key, result);
    }
  }

  public static void main(String[] args) throws Exception {
    Configuration conf = new Configuration();
    Job job = Job.getInstance(conf, "word count");
    job.setJarByClass(WordCount.class);
    job.setMapperClass(TokenizerMapper.class);
    job.setCombinerClass(IntSumReducer.class);
    job.setReducerClass(IntSumReducer.class);
    job.setOutputKeyClass(Text.class);
    job.setOutputValueClass(IntWritable.class);
    FileInputFormat.addInputPath(job, new Path(args[0]));
    FileOutputFormat.setOutputPath(job, new Path(args[1]));
    System.exit(job.waitForCompletion(true) ? 0 : 1);
  }
}

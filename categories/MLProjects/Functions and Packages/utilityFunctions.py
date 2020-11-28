# -*- coding: utf-8 -*-
# -- ==Display Data Frames side by side== --
class utilityFunc():
    
    # -- ==Display Data Frames side by side== --
    class display(object):
        """
        
        Display HTML representation of multiple objects
        
        PARAMETERS
        ----------
        Takes string arguments relating to DataFrame variables, comma separated
        
        RETURNS
        -------
        An attractive output of the DataFrames
        
        
        """
        template = """<div style="float: left; padding: 10px;">
        <p style='font-family:"Courier New", Courier, monospace'>{0}</p>{1}
        </div>"""
        def __init__(self, *args):
            self.args = args
            
        def _repr_html_(self):
            return '\n'.join(self.template.format(a, eval(a)._repr_html_())
                             for a in self.args)
        
        def __repr__(self):
            return '\n\n'.join(a + '\n' + repr(eval(a))
                               for a in self.args)
    
    
    # -- ==Easy DataFrame creation== --
    def make_df(cols, ind):
        """
        Quickly make a DataFrame
        
        PARAMETERS
        -----------
        Takes columns and indices
        
        RETURNS
        -------
        A DataFrame
        
        """
        data = {c: [str(c) + str(i) for i in ind]
                for c in cols}
        return pd.DataFrame(data, ind)
    


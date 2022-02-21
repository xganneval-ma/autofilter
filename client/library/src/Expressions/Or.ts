const Or = (...oprsOrExprs: ExpressionLink['children']): ExpressionLink => {
    return {
      type: "Or",
      children: oprsOrExprs,
    };
  };
  
  export default Or;
  
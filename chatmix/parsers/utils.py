import re
from typing import Optional, Dict, Any, List
from bs4 import BeautifulSoup


def extract_code_blocks(html: str) -> List[Dict[str, Any]]:
    """
    Extract code blocks from HTML content.
    
    Args:
        html: The HTML content containing code blocks.
        
    Returns:
        A list of dictionaries containing code blocks with language and content.
    """
    soup = BeautifulSoup(html, 'html.parser')
    code_blocks = []
    
    # Find all pre elements (code blocks)
    pre_elements = soup.find_all('pre')
    
    for pre in pre_elements:
        code_elem = pre.find('code')
        if not code_elem:
            continue
            
        # Try to determine the language
        language = None
        class_attr = code_elem.get('class', [])
        for cls in class_attr:
            if cls.startswith('language-'):
                language = cls.replace('language-', '')
                break
        
        code_blocks.append({
            'language': language,
            'content': code_elem.get_text()
        })
    
    return code_blocks


def extract_lists(html: str) -> List[Dict[str, Any]]:
    """
    Extract lists from HTML content.
    
    Args:
        html: The HTML content containing lists.
        
    Returns:
        A list of dictionaries containing list type and items.
    """
    soup = BeautifulSoup(html, 'html.parser')
    lists = []
    
    # Find all ul and ol elements
    ul_elements = soup.find_all('ul')
    ol_elements = soup.find_all('ol')
    
    for ul in ul_elements:
        items = [li.get_text() for li in ul.find_all('li')]
        lists.append({
            'type': 'unordered',
            'items': items
        })
    
    for ol in ol_elements:
        items = [li.get_text() for li in ol.find_all('li')]
        lists.append({
            'type': 'ordered',
            'items': items
        })
    
    return lists


def extract_tables(html: str) -> List[Dict[str, Any]]:
    """
    Extract tables from HTML content.
    
    Args:
        html: The HTML content containing tables.
        
    Returns:
        A list of dictionaries containing table headers and rows.
    """
    soup = BeautifulSoup(html, 'html.parser')
    tables = []
    
    # Find all table elements
    table_elements = soup.find_all('table')
    
    for table in table_elements:
        headers = []
        rows = []
        
        # Extract headers
        thead = table.find('thead')
        if thead:
            th_elements = thead.find_all('th')
            headers = [th.get_text() for th in th_elements]
        
        # Extract rows
        tbody = table.find('tbody')
        if tbody:
            tr_elements = tbody.find_all('tr')
            for tr in tr_elements:
                row = [td.get_text() for td in tr.find_all('td')]
                rows.append(row)
        
        tables.append({
            'headers': headers,
            'rows': rows
        })
    
    return tables


def extract_headings(html: str) -> List[Dict[str, Any]]:
    """
    Extract headings from HTML content.
    
    Args:
        html: The HTML content containing headings.
        
    Returns:
        A list of dictionaries containing heading level and text.
    """
    soup = BeautifulSoup(html, 'html.parser')
    headings = []
    
    # Find all heading elements (h1-h6)
    for level in range(1, 7):
        tag = f'h{level}'
        for heading in soup.find_all(tag):
            headings.append({
                'level': level,
                'text': heading.get_text()
            })
    
    return headings


def html_to_markdown(html: str) -> str:
    """
    Convert HTML content to Markdown format.
    
    Args:
        html: The HTML content to convert.
        
    Returns:
        The converted Markdown text.
    """
    # This is a simplified implementation
    # For a complete solution, consider using a dedicated library
    
    soup = BeautifulSoup(html, 'html.parser')
    
    # Replace headings
    for level in range(1, 7):
        tag = f'h{level}'
        for heading in soup.find_all(tag):
            heading_text = heading.get_text()
            heading.replace_with(f"{'#' * level} {heading_text}\n\n")
    
    # Replace lists
    for ul in soup.find_all('ul'):
        items = []
        for li in ul.find_all('li'):
            items.append(f"- {li.get_text()}")
        ul.replace_with("\n".join(items) + "\n\n")
    
    for ol in soup.find_all('ol'):
        items = []
        for i, li in enumerate(ol.find_all('li')):
            items.append(f"{i+1}. {li.get_text()}")
        ol.replace_with("\n".join(items) + "\n\n")
    
    # Replace code blocks
    for pre in soup.find_all('pre'):
        code = pre.find('code')
        if code:
            language = ""
            class_attr = code.get('class', [])
            for cls in class_attr:
                if cls.startswith('language-'):
                    language = cls.replace('language-', '')
                    break
            
            code_text = code.get_text()
            pre.replace_with(f"```{language}\n{code_text}\n```\n\n")
    
    # Replace inline code
    for code in soup.find_all('code'):
        if code.parent.name != 'pre':
            code_text = code.get_text()
            code.replace_with(f"`{code_text}`")
    
    # Replace links
    for a in soup.find_all('a'):
        href = a.get('href', '')
        text = a.get_text()
        a.replace_with(f"[{text}]({href})")
    
    # Replace images
    for img in soup.find_all('img'):
        alt = img.get('alt', '')
        src = img.get('src', '')
        img.replace_with(f"![{alt}]({src})")
    
    # Replace paragraphs
    for p in soup.find_all('p'):
        p_text = p.get_text()
        p.replace_with(f"{p_text}\n\n")
    
    # Get the text and clean up
    markdown = soup.get_text()
    
    # Clean up extra whitespace
    markdown = re.sub(r'\n{3,}', '\n\n', markdown)
    
    return markdown.strip()

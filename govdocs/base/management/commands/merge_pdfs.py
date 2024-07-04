# app/management/commands/merge_pdfs.py
from django.core.management.base import BaseCommand
from django.db.models import Q
from base.models import Document
from django.conf import settings
from PyPDF2 import PdfMerger
import os

class Command(BaseCommand):
    help = 'Merges PDFs with similar names where one has an extra "v", removes their database entries, and adds the merged file back into the database'

    def handle(self, *args, **options):
        docs = Document.objects.all()
        merged_count = 0

        for doc in docs:
            doc_name = str(doc.doc_id)
            a='0001v'
            b='001V'
            c='0001V'
            if a in doc_name or b in doc_name or c in doc_name:
                if a in doc_name:
                    no_v_doc_id = doc_name.replace('0001v', '0001')
                elif b in doc_name:
                    no_v_doc_id = doc_name.replace('001V', '001')
                elif c in doc_name:
                    no_v_doc_id = doc_name.replace('0001V', '0001')
                    
                    
                matching_docs = Document.objects.filter(doc_id=no_v_doc_id)

                if matching_docs.exists():
                    matching_doc = matching_docs.first()

                    # Paths for original and matching documents
                    original_path = os.path.join(settings.MEDIA_ROOT, doc.doc.file.name)
                    matching_path = os.path.join(settings.MEDIA_ROOT, matching_doc.doc.file.name)
                    merger = PdfMerger()

                    try:
                        with open(original_path, 'rb') as original_file, open(matching_path, 'rb') as matching_file:
                            merger.append(original_file)
                            merger.append(matching_file)

                        # Save the merged PDF
                        merged_file_name = f"{no_v_doc_id}_merged.pdf"
                        merged_path = os.path.join(settings.MEDIA_ROOT, merged_file_name)
                        with open(merged_path, 'wb') as merged_file:
                            merger.write(merged_file)

                        print(f"Merged {doc_name} and {no_v_doc_id} into {merged_path}")

                        # Add the merged document to the database
                        new_doc = Document(
                            doc=f'{merged_file_name}',  # Adjust path as needed
                            doc_id=f"{no_v_doc_id}_merged",
                            doc_type=doc.doc_type,
                        )
                        new_doc.save()
                        print(f"Added merged document to database with ID {new_doc.doc_id}")

                        # Delete the original Document entries from the database
                        doc.delete()
                        matching_doc.delete()
                        print(f"Deleted database entries for {doc_name} and {no_v_doc_id}")

                        merged_count += 1

                    except Exception as e:
                        print(f"Failed to merge, delete files, or delete database entries for {doc_name} and {no_v_doc_id}: {str(e)}")
                    finally:
                        merger.close()

        print(f"Total merged documents: {merged_count}")
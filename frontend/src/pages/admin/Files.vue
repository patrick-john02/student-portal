<script lang="ts">
export const description = "Files manager page"
export const iframeHeight = "800px"
export const containerClass = "w-full h-full"
</script>

<script setup lang="ts">
import { ref } from "vue"

import AppSidebar from "@/components/sidebars/AppSidebar.vue"
import {
  SidebarProvider,
  SidebarInset,
  SidebarTrigger,
} from "@/components/ui/sidebar"

import {
  Breadcrumb,
  BreadcrumbList,
  BreadcrumbItem,
  BreadcrumbPage,
  BreadcrumbSeparator,
  BreadcrumbLink,
} from "@/components/ui/breadcrumb"

import { Separator } from "@/components/ui/separator"

import {
  Card,
  CardHeader,
  CardTitle,
  CardDescription,
  CardContent,
} from "@/components/ui/card"

import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Badge } from "@/components/ui/badge"

import {
  Select,
  SelectTrigger,
  SelectValue,
  SelectItem,
  SelectContent,
} from "@/components/ui/select"

import {
  Table,
  TableHead,
  TableRow,
  TableHeader,
  TableBody,
  TableCell,
} from "@/components/ui/table"

import {
  DropdownMenu,
  DropdownMenuTrigger,
  DropdownMenuContent,
  DropdownMenuSeparator,
  DropdownMenuItem,
  DropdownMenuLabel,
} from "@/components/ui/dropdown-menu"

import {
  File,
  FileImage,
  FileText,
  FileArchive,
  FileCode,
  MoreHorizontal,
  Upload,
  Download,
  Trash2,
} from "lucide-vue-next"

const userRole = "Admin"

const search = ref("")
const fileType = ref("all")

// Dummy file data
const files = ref([
  {
    id: 1,
    name: "EnrollmentForm.pdf",
    type: "pdf",
    size: "245 KB",
    uploadedBy: "Registrar",
    uploadedAt: "2025-01-10",
    icon: FileText,
    color: "text-red-500",
  },
  {
    id: 2,
    name: "SchoolLogo.png",
    type: "image",
    size: "120 KB",
    uploadedBy: "Admin",
    uploadedAt: "2025-01-05",
    icon: FileImage,
    color: "text-blue-500",
  },
  {
    id: 3,
    name: "TeachersList.xlsx",
    type: "excel",
    size: "35 KB",
    uploadedBy: "HR",
    uploadedAt: "2025-01-02",
    icon: File,
    color: "text-green-500",
  },
  {
    id: 4,
    name: "Backup-Jan.zip",
    type: "archive",
    size: "8.2 MB",
    uploadedBy: "System",
    uploadedAt: "2025-01-01",
    icon: FileArchive,
    color: "text-yellow-500",
  },
])
</script>

<template>
  <SidebarProvider>
    <AppSidebar :userRole="userRole" />

    <SidebarInset>
      <!-- Header -->
      <header class="flex h-16 items-center gap-2 px-4">
        <SidebarTrigger class="-ml-2" />
        <Separator orientation="vertical" class="mx-2 h-4" />

        <Breadcrumb>
          <BreadcrumbList>
            <BreadcrumbItem>
              <BreadcrumbLink href="/admin/dashboard">Admin</BreadcrumbLink>
            </BreadcrumbItem>
            <BreadcrumbSeparator />
            <BreadcrumbItem>
              <BreadcrumbPage>Files Manager</BreadcrumbPage>
            </BreadcrumbItem>
          </BreadcrumbList>
        </Breadcrumb>
      </header>

      <!-- Content -->
      <div class="flex flex-1 flex-col gap-4 p-4 pt-0">

        <!-- Header -->
        <div class="flex items-center justify-between">
          <div>
            <h2 class="text-2xl font-bold tracking-tight">Files Manager</h2>
            <p class="text-sm text-muted-foreground">
              Manage uploaded system files and directories.
            </p>
          </div>

          <Button class="flex items-center gap-2">
            <Upload class="h-4 w-4" />
            Upload File
          </Button>
        </div>

        <!-- Filters -->
        <Card>
          <CardHeader>
            <CardTitle>File Filters</CardTitle>
            <CardDescription>
              Filter files by type or search for specific file names.
            </CardDescription>
          </CardHeader>

          <CardContent class="flex flex-col md:flex-row gap-4">

            <Input
              v-model="search"
              placeholder="Search files..."
              class="max-w-xs"
            />

            <Select v-model="fileType">
              <SelectTrigger class="w-40">
                <SelectValue placeholder="File Type" />
              </SelectTrigger>
              <SelectContent>
                <SelectItem value="all">All Types</SelectItem>
                <SelectItem value="pdf">PDF</SelectItem>
                <SelectItem value="image">Images</SelectItem>
                <SelectItem value="excel">Excel</SelectItem>
                <SelectItem value="archive">Archive</SelectItem>
                <SelectItem value="other">Other</SelectItem>
              </SelectContent>
            </Select>

          </CardContent>
        </Card>

        <!-- FILE TABLE -->
        <Card>
          <CardHeader>
            <CardTitle>Files</CardTitle>
            <CardDescription>
              Browse, download, and manage all uploaded files.
            </CardDescription>
          </CardHeader>

          <CardContent>
            <Table>
              <TableHeader>
                <TableRow>
                  <TableHead class="w-64">File Name</TableHead>
                  <TableHead>Uploaded By</TableHead>
                  <TableHead>Size</TableHead>
                  <TableHead>Date</TableHead>
                  <TableHead class="text-right w-20">Actions</TableHead>
                </TableRow>
              </TableHeader>

              <TableBody>
                <TableRow
                  v-for="file in files"
                  :key="file.id"
                  class="hover:bg-muted/50"
                >
                  <!-- File Name -->
                  <TableCell>
                    <div class="flex items-center gap-2">
                      <component
                        :is="file.icon"
                        class="h-4 w-4"
                        :class="file.color"
                      />
                      <span class="font-medium">
                        {{ file.name }}
                      </span>
                    </div>
                  </TableCell>

                  <!-- Uploaded by -->
                  <TableCell class="text-muted-foreground">
                    {{ file.uploadedBy }}
                  </TableCell>

                  <!-- Size -->
                  <TableCell class="text-muted-foreground">
                    {{ file.size }}
                  </TableCell>

                  <!-- Date -->
                  <TableCell class="text-muted-foreground">
                    {{ file.uploadedAt }}
                  </TableCell>

                  <!-- Actions -->
                  <TableCell class="text-right">
                    <DropdownMenu>
                      <DropdownMenuTrigger as-child>
                        <Button variant="ghost" size="icon">
                          <MoreHorizontal class="h-4 w-4" />
                        </Button>
                      </DropdownMenuTrigger>

                      <DropdownMenuContent align="end">
                        <DropdownMenuLabel>Actions</DropdownMenuLabel>
                        <DropdownMenuSeparator />

                        <DropdownMenuItem>
                          <Download class="h-4 w-4 mr-2" />
                          Download
                        </DropdownMenuItem>

                        <DropdownMenuItem class="text-red-600">
                          <Trash2 class="h-4 w-4 mr-2" />
                          Delete File
                        </DropdownMenuItem>

                      </DropdownMenuContent>
                    </DropdownMenu>
                  </TableCell>

                </TableRow>
              </TableBody>
            </Table>
          </CardContent>
        </Card>

      </div>
    </SidebarInset>
  </SidebarProvider>
</template>
